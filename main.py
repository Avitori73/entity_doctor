import cmd
from rich.console import Console
from check_lost import check_entity_lost
from remove_entity import remove_entity

console = Console()


class CLI(cmd.Cmd):
    def __init__(self, completekey="tab", stdin=None, stdout=None):
        super().__init__(completekey, stdin, stdout)
        self.prompt = "entity-doctor> "
        self.intro = "Welcome to Entity Doctor CLI. Type help or ? to list commands."

    def do_rm(self, args):
        """Remove an entity from the project."""
        remove_entity()

    def do_chk_lost(self, args):
        """Check the entity is complete."""
        check_entity_lost()

    def do_exit(self, line):
        return True


if __name__ == "__main__":
    cli = CLI()
    cli.cmdloop()
