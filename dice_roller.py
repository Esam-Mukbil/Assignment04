import random

def roll_dice():
    dice_faces = {
        1: "🎲 One",
        2: "🎲 Two",
        3: "🎲 Three",
        4: "🎲 Four",
        5: "🎲 Five",
        6: "🎲 Six"
    }
    roll = random.randint(1, 6)
    return f"Result: {dice_faces[roll]}"

if __name__ == "__main__":
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        command = input("Type 'roll' to roll the dice or 'exit' to quit: ").strip().lower()
        if command == 'roll':
            print(roll_dice())
        elif command == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please type 'roll' or 'exit'.")
