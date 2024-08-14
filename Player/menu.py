from Utilities.gameOver import endGame
from Utilities.utilities import historyLine
from Player.characterStats import characterStats

def menu(character):
    """
    Displays a menu that allows the player to choose between viewing character stats,
    ending the game, or going back to the previous menu.

    Args:
        character: The character object containing the player's information and stats.
    """
    # Text to display the available menu options
    menu_text = "\nType 1 to view character stats\nType 2 to open Inventory\nType 3 to end game\nType 4 to go back"
    
    # Trigger to keep the menu active until a valid option is selected
    trigger = False
    
    # Loop to repeatedly prompt the player for input until they choose to end or go back
    while not trigger:
        historyLine(menu_text)  # Display the menu options
        user_input = input("Choose an option: ")  # Prompt the player for a menu choice
        
        if user_input == "1":  # If the player chooses to view character stats
            characterStats(character)  # Display character stats
        elif user_input == "2":  # If the player chooses to check inventory
            inventory = character.getInventory()
            historyLine("Inventory:\n" + inventory)
        elif user_input == "3":  # If the player chooses to end the game
            endGame(character)  # Call the function to end the game
            trigger = True  # Exit the loop to end the menu
        elif user_input == "4":  # If the player chooses to go back
            trigger = True  # Exit the loop to go back to the previous menu
            return  # Return to the previous function
        else:
            # If the player enters an invalid option, display an error message
            historyLine("\nSorry, please enter a valid option.\n")
