import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.columns import Columns
from rich.prompt import IntPrompt

console = Console()


def read_env():
    # 加载 .env 文件
    load_dotenv()

    # 获取 PJ_ 开头的变量名
    return {
        key[3:]: value for key, value in os.environ.items() if key.startswith("PJ_")
    }


def prompt_to_pick_project():
    env_vars = read_env()
    console.print("Available projects:", style="cyan")
    contents = []
    for i, key in enumerate(env_vars.keys()):
        contents.append(
            Panel(
                f"[cyan]{key}[/]",
                title=f"Index {i}",
                border_style="blue",
                title_align="center",
            )
        )
    console.print(Columns(contents))
    project_index = IntPrompt.ask(
        "Please select a project index [cyan](Range:0 ~ {})".format(len(env_vars) - 1)
    )

    if project_index < 0 or project_index >= len(env_vars):
        console.print("Error: Invalid index.", style="red")
        exit(1)

    project_name = list(env_vars.keys())[project_index]
    return (project_name, env_vars.get(project_name))


if __name__ == "__main__":
    console.print(prompt_to_pick_project())
