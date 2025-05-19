from detect_entity import detect_source_path, list_entity
from rich.console import Console
from rich.panel import Panel

from read_env import prompt_to_pick_project

console = Console()

entity_regex = r"(\w+)(?<!Key)\.java"
entity_key_regex = r"(\w+)Key.java"
entity_repository_regex = r"(\w+)Repository.java"
entity_vo_regex = r"(\w+)VO.java"


def check_entity_lost():
    project_name, project_path = prompt_to_pick_project()
    source_path = detect_source_path(project_path)
    check_lost(source_path)


def check_lost(source_path):
    entity_set = list_entity(entity_regex, source_path["entity"]["entity_path"])
    entity_partition_set = list_entity(
        entity_regex, source_path["entity"]["entity_partition_path"]
    )
    entity_partition_key_set = list_entity(
        entity_key_regex, source_path["entity"]["entity_partition_path"]
    )
    repository_set = list_entity(
        entity_repository_regex, source_path["repository"]["repository_path"]
    )
    repository_partition_set = list_entity(
        entity_repository_regex,
        source_path["repository"]["repository_partition_path"],
    )
    vo_set = list_entity(entity_vo_regex, source_path["vo"]["vo_path"])
    vo_partition_set = list_entity(
        entity_vo_regex, source_path["vo"]["vo_partition_path"]
    )
    is_any_lost = get_lost_report(
        {
            "Entity": entity_set,
            "Repository": repository_set,
            "VO": vo_set,
        }
    )
    is_any_partition_lost = get_lost_report(
        {
            "Entity Partition": entity_partition_set,
            "Entity Partition Key": entity_partition_key_set,
            "Repository Partition": repository_partition_set,
            "VO Partition": vo_partition_set,
        }
    )
    if not is_any_lost and not is_any_partition_lost:
        console.print("No lost entities found in the project.", style="green")


def get_lost_report(type_to_set: dict):
    any_lost = False
    common_set = set.intersection(*type_to_set.values())
    lost_contents = []
    for type_name, entity_set in type_to_set.items():
        lost_set = entity_set - common_set
        if lost_set:
            lost_contents.append(
                Panel(
                    f"{', '.join(lost_set)}",
                    title=f"Lost {type_name} entities",
                    title_align="left",
                    border_style="red",
                )
            )
            any_lost = True

    console.print(*lost_contents)
    return any_lost


if __name__ == "__main__":
    check_entity_lost()
