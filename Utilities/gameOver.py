from Player.characterStats import characterStats
from Utilities.utilities import historyLine, getFile
from Utilities.fileOrganizer import fileChecker
from Services.gmailProvider import gmail_send_message
def endGame(character):
    endGameDialogue = "\n\nThe game has ended. Thank you for playing Venequia\n\nYour character finished with the following stats:\n"
    historyLine(endGameDialogue)
    characterStats(character)
    #gmail_send_message("Hola","Chart story",character.getEmail(),getFile())
    fileChecker()
    
    