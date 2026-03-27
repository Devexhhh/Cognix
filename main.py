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

        # Ignore silence / noise
        if not user_input:
            continue

        user_input = user_input.strip()
        lower_input = user_input.lower()

        if lower_input == "exit":
            print("[bold red]Shutting down Cognix.[/bold red]")
            break

        print(f"[bold green]You:[/bold green] {user_input}")

        # ------------------------
        # MEMORY: remember name
        # ------------------------
        if "my name is" in lower_input:

            name = lower_input.replace("my name is", "").strip().title()

            memory.remember("username", name)

            reply = f"Nice to meet you, {name}."

            print("[bold cyan]Cognix:[/bold cyan]", reply)
            voice.speak(reply)

            continue

        # ------------------------
        # MEMORY: recall name
        # ------------------------
        if "what is my name" in lower_input:

            name = memory.recall("username")

            if name:
                reply = f"Your name is {name}."
            else:
                reply = "I don't know your name yet."

            print("[bold cyan]Cognix:[/bold cyan]", reply)
            voice.speak(reply)

            continue

        # ------------------------
        # AI BRAIN
        # ------------------------
        reply = cognix.think(user_input)

        # ------------------------
        # ACTION SYSTEM
        # ------------------------
        if reply.startswith("ACTION:"):

            action = reply.replace("ACTION:", "").strip()

            result = actions.execute(action)

            if result:
                reply = result
            else:
                reply = "I couldn't perform that action."

        # ------------------------
        # CLEAN RESPONSE
        # ------------------------
        if "no action necessary" in reply.lower():
            reply = "Hello. How can I assist you?"

        print("[bold cyan]Cognix:[/bold cyan]", reply)
        voice.speak(reply)


if __name__ == "__main__":
    main()