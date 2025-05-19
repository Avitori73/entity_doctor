import os
import re
from main_console import console
from rich.panel import Panel
from read_env import prompt_to_pick_project
import stringcase as sc

WORK_PATH = "src\\main\\java\\com\\a1stream\\domain"
DOMAIN_NAME = "a1stream-domain"
ENTITY_FOLDER = "entity"
REPOSITORY_FOLDER = "repository"
VO_FOLDER = "vo"
PARTITION_FOLDER = "partition"


def search_entity(entity_name, source_path, project_path):
    exist_source = find_entity_file(entity_name, source_path)
    if not exist_source:
        console.print(f"Entity file not found for {entity_name}.", style="red")
        return None

    print_info(entity_name, project_path)
    print_exist_source(exist_source)
    return exist_source


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
    entity_source = look_up_files(
        [f"{entity_name}.java", f"{entity_name}Key.java"],
        [
            source_path_entity["entity_path"],
            source_path_entity["entity_partition_path"],
        ],
    )
    exist_source.extend(entity_source)

    # check repository
    source_path_repository = source_path["repository"]
    repository_source = look_up_files(
        [f"{entity_name}Repository.java"],
        [
            source_path_repository["repository_path"],
            source_path_repository["repository_partition_path"],
        ],
    )
    exist_source.extend(repository_source)

    # check vo
    source_path_vo = source_path["vo"]
    vo_source = look_up_files(
        [f"{entity_name}VO.java"],
        [
            source_path_vo["vo_path"],
            source_path_vo["vo_partition_path"],
        ],
    )
    exist_source.extend(vo_source)

    return exist_source


def look_up_files(filenames, paths):
    found_files = []
    for filename in filenames:
        for path in paths:
            file_path = os.path.join(path, filename)
            if os.path.exists(file_path):
                found_files.append((filename, file_path))
    return found_files


def print_exist_source(exist_source):
    contents = []
    for name, source_path in exist_source:
        # source_path 从 a1stream-domain 开始前面的路径截断
        source_path = f"..\\{DOMAIN_NAME}{source_path.split(DOMAIN_NAME)[-1]}"
        contents.append(
            Panel(
                f"[cyan]Path: {source_path}[/]",
                title=f"{name}",
                border_style="green",
                title_align="left",
            )
        )
    console.print(*contents)


def print_info(entity_name, project_path):
    console.print(
        f"""
Entity file exists in the following paths

[INFO]
Entity Name: [green]{entity_name}[/]
Root Path: [green]{project_path}[/]
""",
        style="cyan",
    )


def list_entity(regex, source_path):
    entity = set()
    for file in os.listdir(source_path):
        if file.endswith(".java"):
            match = re.search(regex, file)
            if match:
                entity.add(match.group(1))

    return entity


if __name__ == "__main__":
    choose_project = prompt_to_pick_project()
    if choose_project is None:
        exit(1)
    _, project_path = choose_project
    source_path = detect_source_path(project_path)
    entity_name = str(console.input("Please input entity name: "))
    entity_name = sc.camelcase(entity_name)
    search_entity(entity_name, source_path, project_path)
