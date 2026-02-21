from brain import Brain
from rich import print

def main():

    jarvis = Brain()

    print("[bold cyan]Jarvis initialized.[/bold cyan]")
    print("[bold yellow]Type 'exit' to quit.[/bold yellow]\n")

    while True:
        print("[bold green]You:[/bold green]", end="")
        user_input = input()

        if user_input.lower() == "exit":
            print("[bold red]Jarvis shutting down.[/bold red]")
            break

        print("[bold cyan]Jarvis:[/bold cyan] ", end="")

        jarvis.think(user_input)
        print()


if __name__ == "__main__":
    main()