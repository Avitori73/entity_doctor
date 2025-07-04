import stringcase as sc
import pyperclip as pc
from rich.prompt import IntPrompt, Prompt
from rich.panel import Panel
from rich.columns import Columns
from .main_console import console


def change_case():
    """Change the case of the entity name."""
    entity_name = Prompt.ask("Enter the entity name")
    if not entity_name:
        console.print("[bold red]Entity name cannot be empty.[/bold red]")
        return

    console.print("[cyan]Select the case you want to change to:")
    contents = []
    contents.append(
        Panel(
            "snake_case",
            title="1",
            border_style="bold blue",
            title_align="left",
        )
    )
    contents.append(
        Panel(
            "camelCase",
            title="2",
            border_style="bold blue",
            title_align="left",
        )
    )
    contents.append(
        Panel(
            "PascalCase",
            title="3",
            border_style="bold blue",
            title_align="left",
        )
    )
    contents.append(
        Panel(
            "kebab-case",
            title="4",
            border_style="bold blue",
            title_align="left",
        )
    )
    console.print(Columns(contents))
    choices = [str(i) for i in range(1, 5)]
    case = IntPrompt.ask("Enter the case number", choices=choices)

    if str(case) in choices:
        if case == 1:
            new_entity_name = snakelize(entity_name)  # Convert to snake_case
        elif case == 2:
            new_entity_name = camelize(entity_name)  # Convert to camelCase
        elif case == 3:
            new_entity_name = pascalize(entity_name)  # Convert to PascalCase
        elif case == 4:
            new_entity_name = kebabize(entity_name)  # Convert to kebab-case
        pc.copy(new_entity_name)
        console.print(
            f"[bold green]New entity name [bold blue]({new_entity_name})[/bold blue] copied to clipboard.[/bold green]"
        )
    else:
        console.print("[bold red]Invalid case number.[/bold red]")


def camelize(entity_name):
    """Convert to camelCase."""
    return sc.camelcase(entity_name)


def pascalize(entity_name):
    """Convert to PascalCase."""
    return sc.pascalcase(entity_name)


def snakelize(entity_name):
    """Convert to snake_case."""
    return sc.snakecase(entity_name)


def kebabize(entity_name):
    """Convert to kebab-case."""
    return sc.spinalcase(entity_name)
