import os
import tempfile
import subprocess
from .main_console import console


def add_entity():
    temp_dir = os.path.join(os.getcwd(), "temp")
    os.makedirs(temp_dir, exist_ok=True)

    # create a temporary file
    fd, temp_path = tempfile.mkstemp(dir=temp_dir, suffix=".sql")
    filename = os.path.basename(temp_path)
    os.close(fd)  # close file descriptor

    # open file with default editor
    if os.name == "nt":
        os.system(f'start "" "{temp_path}"')
    else:
        os.system(f'open "{temp_path}"')

    console.print(
        "[cyan]Waiting for you to edit file...",
    )

    # wait for user to finish editing
    console.input("Press [bold green]Enter[/bold green] after editing.")

    # run egg.ps1 script in temp directory
    subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "egg", "-f", filename],
        stdin=subprocess.PIPE,
        cwd=temp_dir,
    )

    # delete temporary file
    os.remove(temp_path)


if __name__ == "__main__":
    add_entity()
