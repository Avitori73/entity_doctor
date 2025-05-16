import os
from rich.console import Console
from read_env import prompt_to_pick_project

console = Console()

WORK_PATH = "src\\main\\java\\com\\a1stream\\domain"
DOMAIN_NAME = "a1stream-domain"
ENTITY_FOLDER = "entity"
REPOSITORY_FOLDER = "repository"
VO_FOLDER = "vo"
PARTITION_FOLDER = "partition"


def detect_source_path(project_path):
    domain_path = os.path.join(project_path, DOMAIN_NAME)
    entity_path = os.path.join(domain_path, WORK_PATH, ENTITY_FOLDER)
    repository_path = os.path.join(domain_path, WORK_PATH, REPOSITORY_FOLDER)
    vo_path = os.path.join(domain_path, WORK_PATH, VO_FOLDER)
    entity_partition_path = os.path.join(entity_path, PARTITION_FOLDER)
    repository_partition_path = os.path.join(repository_path, PARTITION_FOLDER)
    vo_partition_path = os.path.join(vo_path, PARTITION_FOLDER)

    return {
        "entity": {
            "entity_path": entity_path,
            "entity_partition_path": entity_partition_path,
        },
        "vo": {
            "vo_path": vo_path,
            "vo_partition_path": vo_partition_path,
        },
        "repository": {
            "repository_path": repository_path,
            "repository_partition_path": repository_partition_path,
        },
    }


def find_entity_file(entity_name, source_path):
    exist_source = []
    # check entity
    source_path_entity = source_path["entity"]
    for key in ["entity_path", "entity_partition_path"]:
        entity_file_name = f"{entity_name}.java"
        entity_key_name = f"{entity_name}Key.java"
        entity_file = find_file_in_path(entity_file_name, source_path_entity[key])
        if entity_file:
            exist_source.append(entity_file)
        entity_key_file = find_file_in_path(entity_key_name, source_path_entity[key])
        if entity_key_file:
            exist_source.append(entity_key_file)

    # check repository
    source_path_repository = source_path["repository"]
    for key in ["repository_path", "repository_partition_path"]:
        repository_name = f"{entity_name}Repository.java"
        repository_file = find_file_in_path(
            repository_name, source_path_repository[key]
        )
        if repository_file:
            exist_source.append(repository_file)

    # check vo
    source_path_vo = source_path["vo"]
    for key in ["vo_path", "vo_partition_path"]:
        vo_name = f"{entity_name}VO.java"
        vo_file = find_file_in_path(vo_name, source_path_vo[key])
        if vo_file:
            exist_source.append(vo_file)

    return exist_source


def find_file_in_path(name, path):
    target_file_path = os.path.join(path, name)
    if os.path.exists(target_file_path):
        return (name, target_file_path)
    return None


if __name__ == "__main__":
    project_name, project_path = prompt_to_pick_project()
    source_path = detect_source_path(project_path)
    entity_name = str(console.input("Please input entity name: "))
    exist_source = find_entity_file(entity_name, source_path)
    print("Entity file exists in the following paths:")
    for name, source_path in exist_source:
        console.print(f" - [green]{name}[/]: {source_path}", style="cyan")

    # console.print(source_path)
