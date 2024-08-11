from Utilities.gameOver import endGame
from Utilities.utilities import historyLine
from Player.characterStats import characterStats

def menu(character):
    menu_text = "\nType 1 to view character stats\nType 2 to end game\nType 3 to go back"
    trigger = False
    while not trigger:
        historyLine(menu_text)
        user_input = input("Choose an option: ")
        if user_input == "1":
            characterStats(character)
        elif user_input == "2":
            endGame(character)
            trigger = True
        elif user_input == "3":
            trigger = True
            return
        else:
            historyLine("Sorry, please enter a valid option.")