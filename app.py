from creatures.dragon import Dragon
from creatures.elf import Elf
from creatures.goblin import Goblin
from voice_input import get_voice_input
from text_to_speech import speak_text

def main():
    print("Welcome to the Mythical Creatures AI App!")
    print("Choose your creature:")
    print("1. Dragon")
    print("2. Elf")
    print("3. Goblin")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        creature = Dragon()
        voice = "en-US-GuyNeural"  # Deep male voice for dragon
    elif choice == '2':
        creature = Elf()
        voice = "en-US-JennyNeural"  # Soft female voice for elf
    elif choice == '3':
        creature = Goblin()
        voice = "en-US-RogerNeural"  # Fun voice for goblin
    else:
        print("Invalid choice.")
        return

    intro = creature.introduce()
    print(f"{creature.__class__.__name__}: {intro}")
    speak_text(intro, voice)

    while True:
        print("\n🎤 Speak to the creature (say 'stop' to exit)...")
        user_input = get_voice_input()

        if user_input is None:
            break

        response = creature.respond(user_input)
        print(f"{creature.__class__.__name__}: {response}")
        speak_text(response, voice)

if __name__ == "__main__":
    main()
