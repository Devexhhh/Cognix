from brain import Brain
from actions import Actions
from rich import print

def main():

    cognix = Brain()
    actions = Actions()

    print("[bold cyan]Cognix initialized.[/bold cyan]\n")

    while True:

        print("[bold green]You:[/bold green] ", end="")
        user_input = input()

        if user_input.lower() == "exit":
            break

        reply = cognix.think(user_input)

        # Detect action command
        if reply.startswith("ACTION:"):

            action = reply.replace("ACTION:", "").strip()

            result = actions.execute(action)

            print("[bold cyan]Cognix:[/bold cyan]", result)

        else:

            print("[bold cyan]Cognix:[/bold cyan]", reply)


if __name__ == "__main__":
    main()