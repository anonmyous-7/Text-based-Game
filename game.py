import time

# --- Utilities ---
def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    print("\n" * 100)

# --- Data Structures ---
class Character:
    def __init__(self, name, char_class, inventory=None):
        self.name = name
        self.char_class = char_class
        self.inventory = inventory if inventory else []

class Game:
    def __init__(self):
        self.character = None
        self.running = True

# --- Game Functions ---
def create_character():
    clear_screen()
    slow_print("Welcome to the world of Pythonia!")
    time.sleep(1)
    slow_print("Before we begin, let's create your character.")
    
    name = input("Enter your character's name: ")
    char_class = input("Choose your class (Warrior/Mage/Rogue): ")
    
    return Character(name, char_class)

def main_menu(game):
    clear_screen()
    slow_print(f"Welcome, {game.character.name} the {game.character.char_class}!")
    slow_print("What would you like to do?")
    slow_print("1. Start Adventure")
    slow_print("2. View Inventory")
    slow_print("3. Exit Game")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        start_adventure(game)
    elif choice == '2':
        view_inventory(game)
    elif choice == '3':
        game.running = False
    else:
        slow_print("Invalid choice. Please try again.")
        main_menu(game)

def view_inventory(game):
    clear_screen()
    if not game.character.inventory:
        slow_print("Your inventory is empty.")
    else:
        slow_print("Your inventory contains:")
        for item in game.character.inventory:
            slow_print(f"- {item}")
    input("Press Enter to return to the main menu...")
    main_menu(game)

def start_adventure(game):
    clear_screen()
    slow_print("Your adventure begins in the small village of Nython...")
    slow_print("As you explore the village, you encounter an old man.")
    slow_print("Old Man: 'Greetings, traveler! Could you help me with a task?'")
    slow_print("1. Help the old man")
    slow_print("2. Ignore the old man")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        help_old_man(game)
    elif choice == '2':
        ignore_old_man(game)
    else:
        slow_print("Invalid choice. Please try again.")
        start_adventure(game)

def help_old_man(game):
    clear_screen()
    slow_print("Old Man: 'Thank you, kind traveler! I lost my walking stick in the forest.'")
    slow_print("Old Man: 'Could you find it for me? It should be near the big oak tree.'")
    slow_print("You decide to venture into the forest.")
    slow_print("After a while, you find the old man's walking stick near the big oak tree.")
    slow_print("You return to the village and give the stick to the old man.")
    slow_print("Old Man: 'Thank you! Here, take this potion as a reward.'")
    game.character.inventory.append("Potion")
    slow_print("You received a Potion!")
    input("Press Enter to continue your adventure...")
    start_adventure(game)

def ignore_old_man(game):
    clear_screen()
    slow_print("You decide to ignore the old man and continue exploring the village.")
    slow_print("As you walk away, you notice a strange light coming from the forest.")
    slow_print("1. Investigate the light")
    slow_print("2. Ignore the light and leave the village")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        investigate_light(game)
    elif choice == '2':
        leave_village(game)
    else:
        slow_print("Invalid choice. Please try again.")
        ignore_old_man(game)

def investigate_light(game):
    clear_screen()
    slow_print("You decide to investigate the strange light.")
    slow_print("As you enter the forest, the light grows brighter.")
    slow_print("Suddenly, you find yourself in front of a glowing portal.")
    slow_print("1. Enter the portal")
    slow_print("2. Turn back and leave the forest")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        enter_portal(game)
    elif choice == '2':
        turn_back(game)
    else:
        slow_print("Invalid choice. Please try again.")
        investigate_light(game)

def enter_portal(game):
    clear_screen()
    slow_print("You decide to enter the portal.")
    slow_print("You find yourself in a strange new world...")
    slow_print("To be continued...")
    game.running = False

def turn_back(game):
    clear_screen()
    slow_print("You decide to turn back and leave the forest.")
    start_adventure(game)

def leave_village(game):
    clear_screen()
    slow_print("You decide to leave the village and continue your journey.")
    slow_print("As you walk down the road, you encounter a band of thieves.")
    slow_print("1. Fight the thieves")
    slow_print("2. Run away")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        fight_thieves(game)
    elif choice == '2':
        run_away(game)
    else:
        slow_print("Invalid choice. Please try again.")
        leave_village(game)

def fight_thieves(game):
    clear_screen()
    slow_print("You decide to fight the thieves.")
    slow_print("After a tough battle, you defeat them and find some gold.")
    game.character.inventory.append("Gold")
    slow_print("You received Gold!")
    input("Press Enter to continue your journey...")
    start_adventure(game)

def run_away(game):
    clear_screen()
    slow_print("You decide to run away from the thieves.")
    slow_print("You manage to escape, but you feel ashamed for not standing your ground.")
    start_adventure(game)

# --- Main Game Loop ---
def main():
    game = Game()
    game.character = create_character()
    
    while game.running:
        main_menu(game)
    
    slow_print("Thank you for playing! Goodbye.")

if __name__ == "__main__":
    main()
