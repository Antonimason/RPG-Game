import os;
from dotenv import load_dotenv
from characterClass import Paladin, Knight, Sorcerer, Druid
from enemyClass import Rat, Dog, Elf, Soldier, Orc, Dragon, Hydra, Demon
from Battle import battle
from utilities import recordDocument, emailChecker

def main():
    
    #Dialogue
    emailAddressRequest = "Please introduce an email address in order to send the history of your journey to your mailbox. Remember that your email address must be valid || type 'exit' to exit the game \n"
    welcome = "Welcome to character creation game! \n There will be some questions for you in order to create your character, are you ready? || Type: 'yes' or 'no' \n"
    nameRequest = "Please introduce your character name: || Type 'exit' to exit the game \n"
    genderRequest = "Please introduce the character gender: || Type 'male' or 'female' || type 'exit' to exit the game \n"
    professionRequest = "Please select one of the following professions for your character: \nType 1 to select Paladin \nType 2 to select Knight, \nType 3 to select Sorcerer, \nType 4 to select Druid || type 'exit' to exit the game\n"
    # Loading .env file
    load_dotenv()
    
    def characterCreation():
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
            
            userEmailAddress = input(emailAddressRequest).lower().strip()
            if not emailChecker(userEmailAddress):
                print("Sorry, email address is not valid")
                continue
            if userEmailAddress == "exit":
                trigger = True
                break
                
            characterName = input(nameRequest)
            if characterName.lower().strip() == "exit" or "":
                trigger = True
                break
                
            characterGender = input(genderRequest).lower().strip()
            if characterGender == "exit":
                trigger = True
                break
            if characterGender != "male" or characterGender != "female":
                print("Sorry, gender is not valid")
                continue
                
            characterProfession = input(professionRequest).lower().strip()
            if characterProfession == "1":
                character = Paladin(characterName,characterGender,1,0,300,300,100,30,45,40,10,0)
                chapter_1(character)
                trigger = True
            elif characterProfession == "2":
                character = Knight(characterName,characterGender,1,0,450,450,100,30,45,40,10,0)
                chapter_1(character)
                trigger = True
            elif characterProfession == "3":
                character = Sorcerer(characterName,characterGender,1,0,200,200,100,30,45,40,10,0)
                chapter_1(character)
                trigger = True
            elif characterProfession == "4":
                character = Druid(characterName,characterGender,1,0,200,200,100,30,45,40,10,0)
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
            
    
    def chapter_1(character):
        luneraBeggining = f"\nGood morning, {character.getName()}. This morning you will be asked to do some tasks and completing some duels with differents enemies"
        print(luneraBeggining)
        characterStats(character)
        battle(character,Dog())
        pass
    
    def characterStats(character):
        stats = f"\n------{character.getName()}------\n| Gender: {character.getGender()} |\n| Level: {character.getLevel()} |\n| Exp: {character.getExp()} |\n| |\n| Gold: {character.getGold()} |\n|Max Heatlh: {character.getMaxHealth()} |\n| Current Health: {character.getCurrentHealth()} |\n| Mana: {character.getMana()} |\n| Attack: {character.getAttack()} |\n| Special Attack: {character.getSpecialAttack()} |\n| Defense: {character.getDefense()} |\n| Healing: {character.getHealing()} |\n----------------\n "
        print(stats)
        recordDocument(stats)
            
    #Starting character creation process
    characterCreation()
 
    
if __name__ == "__main__":
    main()
