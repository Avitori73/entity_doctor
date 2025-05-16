from detect_entity import detect_source_path, find_entity_file
from rich.console import Console
from read_env import prompt_to_pick_project
import os

console = Console()


def remove_entity():
    project_name, project_path = prompt_to_pick_project()
    source_path = detect_source_path(project_path)
    entity_name = console.input(
        "[cyan]Please enter the entity name you want to remove (e.g., User): "
    )
    exist_source = find_entity_file(entity_name, source_path)

    if not exist_source:
        console.print(f"Entity file not found for {entity_name}.", style="red")
        return

    print("Entity file exists in the following paths:")
    for name, source_path in exist_source:
        console.print(f" - [green]{name}[/]: {source_path}", style="cyan")

    while True:
        confirm = console.input(
            "Do you want to remove the entity from the above paths? (y/n): "
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
