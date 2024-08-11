import os;
from dotenv import load_dotenv
from Utilities.utilities import historyLine
from Chapters.characterCreation import characterCreation
from Player.characterStats import characterStats
from Services.gmailProvider import gmailProviderCaller


def main():
    
    # Loading .env file
    load_dotenv()
    
    #Starting character creation process
    characterCreation()

    
if __name__ == "__main__":
    main()
