# Mini Text Adventure Game

import random
import time

player_health = 100
player_inventory = []

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def encounter():
    enemies = ["Goblin", "Skeleton", "Wolf"]
    loot = ["Gold Coin", "Health Potion", "Magic Ring"]
    enemy = random.choice(enemies)
    
    slow_print(f"\nA wild {enemy} appears!")
    action = input("Do you want to [F]ight or [R]un? ").lower()
    
    if action == "f":
        if random.random() > 0.5:
            slow_print(f"You defeated the {enemy}!")
            reward = random.choice(loot)
            player_inventory.append(reward)
            slow_print(f"You found a {reward}!")
        else:
            damage = random.randint(5, 20)
            global player_health
            player_health -= damage
            slow_print(f"The {enemy} hit you! You lost {damage} health.")
    else:
        slow_print(f"You ran away safely from the {enemy}.")

def explore():
    slow_print("\nYou venture into the mysterious forest...")
    if random.random() > 0.3:
        encounter()
    else:
        slow_print("You found nothing but beautiful scenery.")

def show_status():
    slow_print(f"\nHealth: {player_health}")
    slow_print(f"Inventory: {player_inventory}")

def main():
    slow_print("Welcome to the Mini Adventure Game!")
    while player_health > 0:
        slow_print("\nWhat do you want to do?")
        print("1. Explore")
        print("2. Show Status")
        print("3. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            explore()
        elif choice == "2":
            show_status()
        elif choice == "3":
            slow_print("Thanks for playing! Goodbye!")
            break
        else:
            slow_print("Invalid choice, try again.")
    
    if player_health <= 0:
        slow_print("You have been defeated! Game Over.")

if __name__ == "__main__":
    main()
