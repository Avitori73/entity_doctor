import cmd
import subprocess
from change_case import change_case
from check_lost import check_entity_lost
from copy_to import copy_to
from remove_entity import remove_entity
from add_entity import add_entity


class CLI(cmd.Cmd):
    def __init__(self, completekey="tab", stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.prompt = "entity-doctor> "
        self.intro = "Welcome to Entity Doctor CLI. Type help or ? to list commands."

    def do_rm(self, args):
        """Remove an entity from the project."""
        remove_entity()

    def do_chk(self, args):
        """Check the entity is complete."""
        check_entity_lost()

    def do_gen(self, args):
        """Generate entity files."""
        add_entity()

    def do_cp2(self, args):
        """Copy files to the project."""
        copy_to()

    def do_cc(self, args):
        """Change Case."""
        change_case()

    def do_sub(self, args):
        """Run a subprocess."""
        subprocess.run(
            ["powershell", "echo", "'Hello from subprocess'"], stdin=subprocess.PIPE
        )

    def do_exit(self, line):
        return True


def main():
    cli = CLI()
    cli.cmdloop()


if __name__ == "__main__":
    main()
