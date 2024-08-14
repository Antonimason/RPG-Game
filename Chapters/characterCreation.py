import re
from .Chapter1 import chapter_1
from Utilities.utilities import recordDocument 
from Player.characterClass import Paladin, Knight, Sorcerer, Druid

def characterCreation():
    """
    Handles the character creation process. 
    The user is prompted to input their email, character name, gender, and profession.
    Depending on the user's choices, a character is created, and the game progresses to chapter 1.
    """
    # Dialogue prompts for user interaction
    emailAddressRequest = "\nPlease introduce an email address in order to send the history of your journey to your mailbox, this email address will be also related to your character\n. Remember that your email address must be valid || type 'exit' to exit the game \n"
    welcome = "\nWelcome to character creation game! \n There will be some questions for you in order to create your character, are you ready? || Type: 'yes' or 'no' \n"
    nameRequest = "\nPlease introduce your character name: || Type 'exit' to exit the game \n"
    genderRequest = "\nPlease introduce the character gender: || Type 'male' or 'female' || type 'exit' to exit the game \n"
    professionRequest = "\nPlease select one of the following professions for your character: \nType 1 to select Paladin \nType 2 to select Knight, \nType 3 to select Sorcerer, \nType 4 to select Druid || type 'exit' to exit the game\n"
    
    # Initialize variables
    startProgram = ""
    userEmailAddress = ""
    characterName = ""
    characterGender = ""
    characterProfession = ""
    character = None
    trigger = False
        
    # Main loop for character creation
    while not trigger:
        startProgram = input(welcome).lower().strip()
        if startProgram == "no":  # Exit if the user does not want to proceed
            trigger = True
            break
            
        userEmailAddress = emailChecker(emailAddressRequest)  # Check for a valid email
        if userEmailAddress is None:  # Exit if the user chooses to exit
            trigger = True
            break
                
        characterName = input(nameRequest)  # Prompt for character name
        if characterName.lower().strip() == "exit" or characterName == "":  # Exit if invalid input
            trigger = True
            break
                
        characterGender = get_valid_gender(genderRequest)  # Get valid gender input
        if characterGender is None:  # Exit if the user chooses to exit
            trigger = True
            break
                 
        characterProfession = input(professionRequest).lower().strip()  # Prompt for character profession
        # Character creation based on chosen profession
        if characterProfession == "1":
            # Paladin(userEmailAddress, characterName, characterGender, profession, level, exp, maxHealth, currentHealth, maxMana, currentMana, attack, specialAttack, defense, healing, gold)
            character = Paladin(userEmailAddress, characterName, characterGender, "Paladin", 1, 0, 100, 300, 300, 100, 100, 30, 45, 40, 10, 0)
            printingCharacterCreation(welcome, startProgram, nameRequest, characterName, genderRequest, characterGender, professionRequest, characterProfession)
            chapter_1(character)  # Start chapter 1 with the created character
            trigger = True
        elif characterProfession == "2":
            # Knight(userEmailAddress, characterName, characterGender, profession, level, exp, maxHealth, currentHealth, maxMana, currentMana, attack, specialAttack, defense, healing, gold)
            character = Knight(userEmailAddress, characterName, characterGender, "Knight", 1, 0, 100, 450, 450, 100, 100, 30, 45, 40, 10, 0)
            printingCharacterCreation(welcome, startProgram, nameRequest, characterName, genderRequest, characterGender, professionRequest, characterProfession)
            chapter_1(character)
            trigger = True
        elif characterProfession == "3":
            # Sorcerer(userEmailAddress, characterName, characterGender, profession, level, exp, maxHealth, currentHealth, maxMana, currentMana, attack, specialAttack, defense, healing, gold)
            character = Sorcerer(userEmailAddress, characterName, characterGender, "Sorcerer", 1, 0, 100, 200, 200, 100, 100, 30, 45, 40, 10, 0)
            printingCharacterCreation(welcome, startProgram, nameRequest, characterName, genderRequest, characterGender, professionRequest, characterProfession)
            chapter_1(character)
            trigger = True
        elif characterProfession == "4":
            # Druid(userEmailAddress, characterName, characterGender, profession, level, exp, maxHealth, currentHealth, maxMana, currentMana, attack, specialAttack, defense, healing, gold)
            character = Druid(userEmailAddress, characterName, characterGender, "Druid", 1, 0, 100, 200, 200, 100, 100, 30, 45, 40, 10, 0)
            printingCharacterCreation(welcome, startProgram, nameRequest, characterName, genderRequest, characterGender, professionRequest, characterProfession)
            chapter_1(character)
            trigger = True
        elif characterProfession == "exit":  # Exit if the user chooses to exit
            trigger = True

def printingCharacterCreation(welcome, startProgram, nameRequest, characterName, genderRequest, characterGender, professionRequest, characterProfession):
    """
    Records the user’s input during the character creation process.
    
    Args:
        welcome (str): The welcome message for character creation.
        startProgram (str): The user's response to starting the character creation process.
        nameRequest (str): The prompt for entering the character's name.
        characterName (str): The user's chosen character name.
        genderRequest (str): The prompt for entering the character's gender.
        characterGender (str): The user's chosen character gender.
        professionRequest (str): The prompt for selecting the character's profession.
        characterProfession (str): The user's chosen character profession.
    """
    recordDocument(welcome)
    recordDocument(startProgram)
    recordDocument(nameRequest)
    recordDocument(characterName)
    recordDocument(genderRequest)
    recordDocument(characterGender)
    recordDocument(professionRequest)
    recordDocument(characterProfession)
    recordDocument(f"\nYour character {characterName} has been created successfully")
                
def get_valid_gender(genderRequest):
    """
    Prompts the user for valid gender input and validates it.
    
    Args:
        genderRequest (str): The prompt for entering the character's gender.
    
    Returns:
        str or None: The valid gender entered by the user, or None if the user exits.
    """
    while True:
        characterGender = input(genderRequest).lower().strip()
        if characterGender == "exit":  # Return None to signal that the user wants to exit
            return None
        if characterGender not in ["male", "female"]:  # Validate gender input
            print("Sorry, gender is not valid. Please enter 'male' or 'female'.")
            continue  # Repeat the question if invalid
        return characterGender  # Return the valid gender
    
def emailChecker(email):
    """
    Validates the email address entered by the user.

    Args:
        email (str): The prompt for entering the user's email address.
    
    Returns:
        str or None: The valid email address entered by the user, or None if the user exits.
    """
    while True:
        userEmailAddress = input(email).lower().strip()
        if userEmailAddress == "exit":  # Return None to signal that the user wants to exit
            return None
        # Regular expression for validating an email address
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        emailMatcher = re.match(email_regex, userEmailAddress)
        # If the email doesn't match the regex, it is invalid
        if not emailMatcher:
            print("Sorry, email address is not valid")
            continue  # Repeat the question if invalid
        return userEmailAddress  # Return the valid email address
