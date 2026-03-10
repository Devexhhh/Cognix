from brain import Brain
from actions import Actions
from rich import print
from memory import Memory

def main():

    cognix = Brain()
    actions = Actions()
    memory = Memory()

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

            # Remember user name
        if "my name is" in user_input.lower():

            name = user_input.lower().replace("my name is", "").strip().title()

            memory.remember("username", name)

            print("[bold cyan]Cognix:[/bold cyan] Nice to meet you", name)

            continue


        # Recall name
        if "what is my name" in user_input.lower():

            name = memory.recall("username")

        if name:
            print("[bold cyan]Cognix:[/bold cyan] Your name is", name)
        else:
            print("[bold cyan]Cognix:[/bold cyan] I don't know your name yet.")

        continue

if __name__ == "__main__":
    main()