from brain import Brain
from actions import Actions
from rich import print
from memory import Memory
from voice import Voice


def main():

    cognix = Brain()
    actions = Actions()
    memory = Memory()
    voice = Voice()

    print("[bold cyan]Cognix initialized.[/bold cyan]\n")

    while True:

        user_input = voice.listen()

        if not user_input:
            continue

        lower_input = user_input.lower()

        if lower_input == "exit":
            print("[bold red]Shutting down Cognix.[/bold red]")
            break

        print(f"[bold green]You:[/bold green] {user_input}")

        # ------------------------
        # MEMORY
        # ------------------------
        if "my name is" in lower_input:
            name = lower_input.replace("my name is", "").strip().title()
            memory.remember("username", name)

            reply = f"Nice to meet you, {name}."
            print("[bold cyan]Cognix:[/bold cyan]", reply)
            voice.speak(reply)
            continue

        if "what is my name" in lower_input:
            name = memory.recall("username")
            reply = f"Your name is {name}." if name else "I don't know your name yet."

            print("[bold cyan]Cognix:[/bold cyan]", reply)
            voice.speak(reply)
            continue

        # ------------------------
        # AI
        # ------------------------
        reply = cognix.think(user_input)

        if reply.startswith("ACTION:"):
            action = reply.replace("ACTION:", "").strip()
            result = actions.execute(action)
            reply = result if result else "I couldn't perform that action."

        if "no action necessary" in reply.lower():
            reply = "Hello. How can I assist you?"

        print("[bold cyan]Cognix:[/bold cyan]", reply)
        voice.speak(reply)


if __name__ == "__main__":
    main()