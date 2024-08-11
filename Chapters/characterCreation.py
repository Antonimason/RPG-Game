import re
from .Chapter1 import chapter_1
from Utilities.utilities import recordDocument 
from Player.characterClass import Paladin, Knight, Sorcerer, Druid

def characterCreation():
    #Dialogue
    emailAddressRequest = "\nPlease introduce an email address in order to send the history of your journey to your mailbox. Remember that your email address must be valid || type 'exit' to exit the game \n"
    welcome = "\nWelcome to character creation game! \n There will be some questions for you in order to create your character, are you ready? || Type: 'yes' or 'no' \n"
    nameRequest = "\nPlease introduce your character name: || Type 'exit' to exit the game \n"
    genderRequest = "\nPlease introduce the character gender: || Type 'male' or 'female' || type 'exit' to exit the game \n"
    professionRequest = "\nPlease select one of the following professions for your character: \nType 1 to select Paladin \nType 2 to select Knight, \nType 3 to select Sorcerer, \nType 4 to select Druid || type 'exit' to exit the game\n"
    startProgram = ""
    userEmailAddress = ""
    characterName = ""
    characterGender = ""
    characterProfession = ""
    character = None
        
    trigger = False
        
    while not trigger:
        startProgram = input(welcome).lower().strip()
        if startProgram == "no":
            trigger = True
            break
            
        userEmailAddress = emailChecker(emailAddressRequest)
        if userEmailAddress == None:
            trigger = True
            break
                
        characterName = input(nameRequest)
        if characterName.lower().strip() == "exit" or "":
            trigger = True
            break
                
        characterGender = get_valid_gender(genderRequest)
        if characterGender == None:
            trigger = True
            break
                 
        characterProfession = input(professionRequest).lower().strip()
        if characterProfession == "1":
            character = Paladin(characterName,characterGender,"Paladin",1,0,300,300,100,100,30,45,40,10,0)
            chapter_1(character)
            trigger = True
        elif characterProfession == "2":
            character = Knight(characterName,characterGender,"Knight",1,0,450,450,100,100,30,45,40,10,0)
            chapter_1(character)
            trigger = True
        elif characterProfession == "3":
            character = Sorcerer(characterName,characterGender,"Sorcerer",1,0,200,200,100,100,30,45,40,10,0)
            chapter_1(character)
            trigger = True
        elif characterProfession == "4":
            character = Druid(characterName,characterGender,"Druid",1,0,200,200,100,100,30,45,40,10,0)
            chapter_1(character)
            trigger = True
        elif characterProfession == "exit":
            trigger = True

        recordDocument(welcome)
        recordDocument(startProgram)
        recordDocument(nameRequest)
        recordDocument(characterName)
        recordDocument(genderRequest)
        recordDocument(characterGender)
        recordDocument(professionRequest)
        recordDocument(characterProfession)
        recordDocument(f"\nYour character {characterName} has been created succesfully")
        
def get_valid_gender(genderRequest):
    while True:
        characterGender = input(genderRequest).lower().strip()
        if characterGender == "exit":
            return None  # Return None to signal that the user wants to exit
        if characterGender not in ["male", "female"]:
            print("Sorry, gender is not valid. Please enter 'male' or 'female'.")
            continue  # Repeat the question
        return characterGender  # Return the valid gender
    
def emailChecker(email):
    while True:
        userEmailAddress = input(email).lower().strip()
        if userEmailAddress == "exit":
            return None
        # Regular expression for validating an Email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        emailMatcher = re.match(email_regex, userEmailAddress)
        # If the email matches the regex, it is valid and return True, otherwise it will return False
        if not emailMatcher:
            print("Sorry, email address is not valid")
            continue
        return userEmailAddress
