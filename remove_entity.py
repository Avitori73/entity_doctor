import humps
from detect_entity import detect_source_path, search_entity
from rich.console import Console
from rich.prompt import Prompt
from read_env import prompt_to_pick_project
import os

console = Console()


def remove_entity():
    project_name, project_path = prompt_to_pick_project()
    source_path = detect_source_path(project_path)
    entity_name = Prompt.ask("Please enter the entity name you want to remove")
    entity_name = humps.camelize(entity_name)
    exist_source = search_entity(entity_name, source_path, project_path)

    if not exist_source:
        return

    while True:
        confirm = Prompt.ask(
            "Do you want to remove the entity from the above paths?",
            choices=["y", "n"],
            show_choices=True,
        )
        if confirm.lower() in ["y", "n"]:
            break
        else:
            console.print("Invalid input. Please enter 'y' or 'n'.", style="red")

    if confirm.lower() == "y":
        for name, source_path in exist_source:
            os.remove(source_path)
            console.print(f"Removed: {name}", style="green")
    else:
        console.print("Operation cancelled.", style="yellow")


if __name__ == "__main__":
    remove_entity()
