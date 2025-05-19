import shutil
from read_env import prompt_to_pick_project
from main_console import console
from common import root_path
import os


def copy_to():
    choose_project = prompt_to_pick_project()
    if choose_project is None:
        return
    _, project_path = choose_project

    temp_output_path = os.path.join(root_path, "temp", "output")
    if not os.path.exists(temp_output_path):
        console.print(
            "[bold red]No temp/output/ directory found. Please run the generate entity command first.[/bold red]"
        )
        return

    subdirs = [entry.name for entry in os.scandir(temp_output_path) if entry.is_dir()]
    copy_path = os.path.join(temp_output_path, subdirs[0]) if subdirs else None
    if not copy_path:
        console.print(
            "[bold red]No subdirectories found in temp/output/. Please run the generate entity command first.[/bold red]"
        )
        return

    all_files = []
    for dirpath, _, filenames in os.walk(copy_path):
        for filename in filenames:
            all_files.append(os.path.join(dirpath, filename))

    for file in all_files:
        # 目标路径
        target_path = os.path.join(
            project_path,
            "a1stream-domain",
            "src",
            "main",
            "java",
            os.path.relpath(file, copy_path),
        )
        # get filename
        filename = os.path.basename(file)
        console.print(f"[bold green]Copying {filename}...[/bold green]")
        shutil.copy2(file, target_path)


if __name__ == "__main__":
    copy_to()
