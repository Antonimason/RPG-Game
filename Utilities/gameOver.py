from Player.characterStats import characterStats
from Utilities.utilities import historyLine

def endGame(character):
    endGameDialogue = "\n\nThe game has ended\n\nYour character finished with the following stats:\n"
    historyLine(endGameDialogue)
    characterStats(character)