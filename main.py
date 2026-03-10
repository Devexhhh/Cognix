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
        
        if reply.startswith("ACTION:"):

            action = reply.replace("ACTION:", "").strip()

            result = actions.execute(action)

            if result:
                print("[bold cyan]Cognix:[/bold cyan]", result)
            else:
                print("[bold cyan]Cognix:[/bold cyan] I couldn't perform that action.")

        else:

            # Filter weird responses
            if "no action necessary" in reply.lower():
                reply = "Hello. How can I assist you?"

            print("[bold cyan]Cognix:[/bold cyan]", reply)

if __name__ == "__main__":
    main()