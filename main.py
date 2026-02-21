from brain import Brain
from rich import print
from actions import Actions

def main():

    jarvis = Brain()
    actions = Actions()

    print("[bold cyan]Cognix initialized.[/bold cyan]")
    print("[bold yellow]Type 'exit' to quit.[/bold yellow]\n")

    while True:
        print("[bold green]You:[/bold green]", end="")
        user_input = input()

        if user_input.lower() == "exit":
            print("[bold red]Cognix shutting down.[/bold red]")
            break

        action_result = actions.execute(user_input)

        if action_result:
            print("[bold cyan]Cognix:[/bold cyan] ", end="")
            print(action_result)
            continue

        print("[bold cyan]Cognix:[/bold cyan] ", end="")
        jarvis.think(user_input)

        print()


if __name__ == "__main__":
    main()