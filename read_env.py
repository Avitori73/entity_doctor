import os
from turtle import st
from dotenv import load_dotenv
from rich.console import Console

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
    for i, key in enumerate(env_vars.keys()):
        console.print(f" - [green]{i}[/]: {key}")
    project_index = int(console.input("Please select a project index: "))

    if project_index < 0 or project_index >= len(env_vars):
        console.print("Error: Invalid index.", style="red")
        exit(1)

    project_name = list(env_vars.keys())[project_index]
    return (project_name, env_vars.get(project_name))


if __name__ == "__main__":
    console.print(prompt_to_pick_project())
