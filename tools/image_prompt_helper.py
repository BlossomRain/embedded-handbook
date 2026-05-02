#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import webbrowser
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPTS_FILE = ROOT / "docs" / "IMAGE_REGEN_PROMPTS.md"
CHATGPT_URL = "https://chatgpt.com/"


@dataclass
class PromptTask:
    index: int
    title: str
    target_path: Path
    current_path: Path
    prompt: str

    @property
    def key(self) -> str:
        slug = re.sub(r"[^a-z0-9]+", "-", self.title.lower()).strip("-")
        return f"{self.index:02d}-{slug}"

    @property
    def status(self) -> str:
        return "done" if self.target_path.exists() else "pending"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_tasks() -> list[PromptTask]:
    text = read_text(PROMPTS_FILE)
    blocks = re.split(r"^###\s+", text, flags=re.MULTILINE)
    tasks: list[PromptTask] = []
    index = 0

    for block in blocks[1:]:
        lines = block.splitlines()
        title = lines[0].strip()

        target_match = re.search(
            r"目标文件：\s*```text\s*(.*?)\s*```", block, flags=re.DOTALL
        )
        current_match = re.search(
            r"当前替换对象：\s*```text\s*(.*?)\s*```", block, flags=re.DOTALL
        )
        prompt_match = re.search(r"提示词：\s*```text\s*(.*?)\s*```", block, flags=re.DOTALL)

        if not (target_match and current_match and prompt_match):
            continue

        index += 1
        target_path = ROOT / target_match.group(1).strip()
        current_path = ROOT / current_match.group(1).strip()
        prompt = prompt_match.group(1).strip()
        tasks.append(
            PromptTask(
                index=index,
                title=title,
                target_path=target_path,
                current_path=current_path,
                prompt=prompt,
            )
        )

    return tasks


def find_task(tasks: list[PromptTask], selector: str) -> PromptTask:
    selector = selector.strip().lower()

    if selector.isdigit():
        idx = int(selector)
        for task in tasks:
            if task.index == idx:
                return task

    for task in tasks:
        if selector == task.key.lower():
            return task

    matches = []
    for task in tasks:
        haystacks = [
            task.title.lower(),
            task.key.lower(),
            task.target_path.relative_to(ROOT).as_posix().lower(),
            task.current_path.relative_to(ROOT).as_posix().lower(),
        ]
        if any(selector in item for item in haystacks):
            matches.append(task)

    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        options = "\n".join(f"- {task.index}: {task.title}" for task in matches)
        raise SystemExit(f"匹配到多个任务，请更具体一些：\n{options}")

    raise SystemExit(f"没有找到任务：{selector}")


def set_clipboard(text: str) -> None:
    command = "Set-Clipboard -Value @'\n" + text + "\n'@"
    subprocess.run(
        ["powershell", "-NoProfile", "-Command", command],
        check=True,
        capture_output=True,
        text=True,
    )


def replace_references(task: PromptTask) -> int:
    old_rel = task.current_path.relative_to(ROOT).as_posix()
    new_rel = task.target_path.relative_to(ROOT).as_posix()
    changed = 0

    for md_path in ROOT.rglob("*.md"):
        text = read_text(md_path)
        if old_rel not in text:
            continue
        new_text = text.replace(old_rel, new_rel)
        if new_text != text:
            md_path.write_text(new_text, encoding="utf-8")
            changed += 1

    return changed


def cmd_list(tasks: list[PromptTask], only_pending: bool) -> int:
    shown = 0
    for task in tasks:
        if only_pending and task.status != "pending":
            continue
        shown += 1
        print(
            f"[{task.index:02d}] {task.status:<7} {task.title}\n"
            f"     key: {task.key}\n"
            f"     target: {task.target_path.relative_to(ROOT).as_posix()}\n"
        )
    if shown == 0:
        print("没有符合条件的任务。")
    return 0


def cmd_show(task: PromptTask) -> int:
    print(f"标题: {task.title}")
    print(f"编号: {task.index}")
    print(f"状态: {task.status}")
    print(f"目标文件: {task.target_path.relative_to(ROOT).as_posix()}")
    print(f"当前替换对象: {task.current_path.relative_to(ROOT).as_posix()}")
    print("\n提示词:\n")
    print(task.prompt)
    return 0


def cmd_copy(task: PromptTask) -> int:
    set_clipboard(task.prompt)
    print(f"已复制提示词：{task.title}")
    return 0


def cmd_open(task: PromptTask | None) -> int:
    if task:
        set_clipboard(task.prompt)
        print(f"已复制提示词：{task.title}")
    webbrowser.open(CHATGPT_URL)
    print(f"已打开：{CHATGPT_URL}")
    return 0


def cmd_import(task: PromptTask, source: Path, move: bool, replace_md: bool) -> int:
    if not source.exists():
        raise SystemExit(f"源文件不存在：{source}")

    task.target_path.parent.mkdir(parents=True, exist_ok=True)

    if move:
        shutil.move(str(source), str(task.target_path))
        action = "移动"
    else:
        shutil.copy2(source, task.target_path)
        action = "复制"

    print(f"已{action}到：{task.target_path.relative_to(ROOT).as_posix()}")

    if replace_md:
        changed = replace_references(task)
        print(f"已更新 Markdown 引用文件数：{changed}")

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Image prompt helper for ChatGPT web generation workflow."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="列出图片任务")
    p_list.add_argument("--pending", action="store_true", help="只看未完成任务")

    p_show = sub.add_parser("show", help="显示某个任务的详细信息")
    p_show.add_argument("selector", help="编号、key 或标题关键字")

    p_copy = sub.add_parser("copy", help="复制某个任务的提示词到剪贴板")
    p_copy.add_argument("selector", help="编号、key 或标题关键字")

    p_open = sub.add_parser("open-chatgpt", help="打开 ChatGPT，并可顺手复制提示词")
    p_open.add_argument("selector", nargs="?", help="编号、key 或标题关键字")

    p_import = sub.add_parser("import", help="把下载图片归档到目标路径")
    p_import.add_argument("selector", help="编号、key 或标题关键字")
    p_import.add_argument("source", help="下载好的源图片路径")
    p_import.add_argument(
        "--copy", action="store_true", help="默认是移动；加这个参数改成复制"
    )
    p_import.add_argument(
        "--replace-md",
        action="store_true",
        help="把仓库里引用旧 SVG 的 Markdown 改成新 PNG",
    )

    return parser


def main(argv: list[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    tasks = parse_tasks()

    if args.command == "list":
        return cmd_list(tasks, only_pending=args.pending)

    if args.command == "show":
        task = find_task(tasks, args.selector)
        return cmd_show(task)

    if args.command == "copy":
        task = find_task(tasks, args.selector)
        return cmd_copy(task)

    if args.command == "open-chatgpt":
        task = find_task(tasks, args.selector) if args.selector else None
        return cmd_open(task)

    if args.command == "import":
        task = find_task(tasks, args.selector)
        source = Path(args.source).expanduser().resolve()
        return cmd_import(task, source, move=not args.copy, replace_md=args.replace_md)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
