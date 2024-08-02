import os;
import gmailProvider as gmail
import fileOrganizer as file
from dotenv import load_dotenv

def main():
    # Cargar el archivo .env
    load_dotenv()
    pass

    def characterCreation():
        trigger = False
        
        while trigger != False:
            startProgram = input("Welcome to character creation game! \n There will be some questions for you in order to create your character, are you ready? || Type: 'yes' or 'no'")
            if startProgram.lower() == 'no':
                trigger = True
            characterName = input("Please introduce your character name: || Type 'exit' if you want to finish the character creation")
            if characterName.lower() == "exit":
                trigger = True
            characterGender = input("Please introduce the character gender: || Type 'male' or 'female' || type 'exit' if you want to finish the character creation")
            if characterGender.lower() == "exit":
                trigger = True
            characterProfesion = input ("Please introduce one of the following professions for your character: Type 'Paladin', 'Knight', 'Sorcerer', 'Druid' || type 'exit' if you want to finish the character creation")
            characterServer = input("Please introduce one of the following servers that the character will be created: Type 'Lunera', 'Fortera', 'Shivera', 'Thundra', 'Solera' || type 'exit' if you want to finish the character creation")
            if characterServer.lower() == "exit":
               trigger = True
        pass

    def createDocument():
        pass

    def gmailProviderCaller():
        pass

    def fileOrganizerCaller():
        pass

main()