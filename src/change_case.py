import humps
import pyperclip as pc
from main_console import console
from rich.prompt import IntPrompt, Prompt
from rich.panel import Panel
from rich.columns import Columns


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
            "camelCase",
            title="1",
            border_style="bold blue",
            title_align="left",
        )
    )
    contents.append(
        Panel(
            "PascalCase",
            title="2",
            border_style="bold blue",
            title_align="left",
        )
    )
    contents.append(
        Panel(
            "snake_case",
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
            new_entity_name = humps.camelize(entity_name)
        elif case == 2:
            new_entity_name = humps.pascalize(entity_name)
        elif case == 3:
            new_entity_name = humps.decamelize(entity_name)
        elif case == 4:
            new_entity_name = humps.kebabize(entity_name)
        pc.copy(new_entity_name)
        console.print(
            f"[bold green]New entity name [bold blue]({new_entity_name})[/bold blue] copied to clipboard.[/bold green]"
        )
    else:
        console.print("[bold red]Invalid case number.[/bold red]")
