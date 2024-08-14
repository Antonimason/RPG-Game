from Player.characterStats import characterStats
from Utilities.utilities import historyLine, getFile
from Utilities.fileOrganizer import fileChecker
from Services.gmailProvider import gmail_send_message

def endGame(character):
    """
    Ends the game, displays the final character stats, sends an email with the story file,
    and organizes the game files.

    Args:
        character: The character object containing the player's information and stats.
    """
    # Dialogue to display when the game ends
    endGameDialogue = "\n\nThe game has ended. Thank you for playing Venequia\n\nYour character finished with the following stats:\n"
    
    # Print the end game dialogue and log it in the history
    historyLine(endGameDialogue)
    
    # Display the final character stats
    characterStats(character)
    
    # Send an email with the game story file to the player's email address
    gmail_send_message("Hola", "Chart story", character.getEmail(), getFile())
    
    # Check and organize game files after the game ends
    fileChecker()

    
    