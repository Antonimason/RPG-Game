from Enemy.enemyClass import Rat, Dog, Elf, Soldier, Orc, Dragon, Hydra, Demon
from Battle.Battle import battle
from Player.menu import menu
from Utilities.utilities import recordDocument
from Utilities.gameOver import historyLine, endGame


def chapter_1(character):
        luneraBeggining = f"\nGood morning, {character.getName()}. This morning you will be asked to do some tasks and completing some duels with differents enemies\nType 1 to keep continue\nType 2 to open menu\n Type 3 to end game\n\n"
        trigger = False
        while not trigger:
            luneraBegginingAnswer = input(luneraBeggining)
            recordDocument(luneraBeggining)
            historyLine(luneraBegginingAnswer)
            
            if luneraBegginingAnswer == "1":
                Awakening(character)
                trigger = True
            elif luneraBegginingAnswer == "2":
                menu(character)
            elif luneraBegginingAnswer == "3":
                endGame(character)
                trigger = True  # This will end the loop
            else:
                historyLine("Please enter a valid option.")
        
def Awakening(character):
    awakening = (
    "The sun has barely risen over the small village of Lunera, where you reside. "
    "The morning mist still clings to the ground, and the chirping of birds fills the air. "
    "Today, however, is not an ordinary day. As you step out of your humble home, "
    "you notice something unusual—no villagers are in sight.\n"
    "Before you can react, a wild dog leaps out from the shadows, its eyes glowing with an unnatural light. "
    "The dog circles you, teeth bared, ready to attack."
    )
    historyLine(awakening)
    battle(character,Dog())
    if not character.getIsAlive():
        endGame(character)
    battle(character,Orc())
    menu(character)
    