from Player.characterStats import characterStats
from Utilities.utilities import historyLine
from Utilities.fileOrganizer import fileChecker
def endGame(character):
    endGameDialogue = "\n\nThe game has ended. Thank you for playing Venequia\n\nYour character finished with the following stats:\n"
    historyLine(endGameDialogue)
    characterStats(character)
    fileChecker()
    
    