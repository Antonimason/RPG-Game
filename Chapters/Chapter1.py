from Enemy.enemyClass import Rat, Dog, Elf, Soldier, Orc, Dragon, Hydra, Demon
from Battle.Battle import battle
from Player.menu import menu
from Utilities.utilities import recordDocument
from Utilities.gameOver import historyLine, endGame

def log_and_record(message, is_input=False):
    """
    Logs and records a message.
    
    Parameters:
    - message: The message to log and record.
    - is_input: If True, logs the message to historyLine.
    """
    if is_input:
        historyLine(message)
    else:
        recordDocument(message)

def get_valid_input(prompt, valid_options):
    """
    Prompts the user for input and ensures it's one of the valid options.
    
    Parameters:
    - prompt: The message displayed to the user.
    - valid_options: A list of valid input options.
    
    Returns:
    - The user's input if it matches a valid option.
    """
    while True:
        user_input = input(prompt)
        if user_input.lower() in valid_options:
            return user_input.lower()
        historyLine("Please enter a valid option.")

def handle_battle(character, enemy):
    """
    Handles the battle process and checks if the character survives.
    
    Parameters:
    - character: The player's character.
    - enemy: The enemy character to battle.
    
    Returns:
    - True if the character is alive after the battle, False otherwise.
    """
    battle(character, enemy)
    if not character.getIsAlive():
        endGame(character)
        return False
    return True

def menuCaller(character, nextEpisode):
    """
    Handles the menu system, allowing the player to continue the story, access the menu, or fight monsters.
    
    Parameters:
    - character: The player's character.
    - nextEpisode: The function to call for the next episode.
    """
    menuText = "Type 1 to continue the story\nType 2 to open menu\nType 3 to kill a monster\n"
    killmonster = "Type 1 to kill a Rat\nType 2 to kill a Dog\nType 3 to kill a Soldier\nType 4 to exit from this menu"
    
    while True:
        menuSelection = get_valid_input(menuText, ["1", "2", "3"])
        log_and_record(menuSelection, is_input=True)
        
        if menuSelection == "1":
            nextEpisode(character)
            break
        elif menuSelection == "2":
            menu(character)
        elif menuSelection == "3":
            while True:
                killSelection = get_valid_input(killmonster, ["1", "2", "3", "4"])
                if killSelection == "1":
                    if handle_battle(character, Rat()):
                        break
                elif killSelection == "2":
                    if handle_battle(character, Dog()):
                        break
                elif killSelection == "3":
                    if handle_battle(character, Soldier()):
                        break
                elif killSelection == "4":
                    break

def chapter_1(character):
    """
    Starts the first chapter of the story.
    
    Parameters:
    - character: The player's character.
    """
    episode = (
        "\n--------------------------------------------------\n"
        "\n-------------------- EPISODE I ---------------------\n"
        "\n--------------------------------------------------\n"
    )
    
    historyLine(episode)
    luneraBeggining = f"\nGood morning, {character.getName()}. This morning you will be asked to do some tasks and completing some duels with different enemies.\nType 1 to continue\nType 2 to open menu\nType 3 to end game\n\n"
    trigger = False
    while not trigger:
        luneraBegginingAnswer = get_valid_input(luneraBeggining, ["1", "2", "3"])
        log_and_record(luneraBegginingAnswer, is_input=True)
            
        if luneraBegginingAnswer == "1":
            Awakening(character)
            trigger = True
        elif luneraBegginingAnswer == "2":
            menu(character)
        elif luneraBegginingAnswer == "3":
            endGame(character)
            trigger = True  # This will end the loop

def Awakening(character):
    """
    The first event of the story where the character is attacked by a dog.
    
    Parameters:
    - character: The player's character.
    """
    awakening = (
    "The sun has barely risen over the small village of Lunera, where you reside. "
    "The morning mist still clings to the ground, and the chirping of birds fills the air. "
    "Today, however, is not an ordinary day. As you step out of your humble home, "
    "you notice something unusual—no villagers are in sight.\n\n"
    "Before you can react, a wild dog leaps out from the shadows, its eyes glowing with an unnatural light. "
    "The dog circles you, teeth bared, ready to attack."
    )
    historyLine(awakening)
    if not handle_battle(character, Dog()):
        return
    menuCaller(character, TheLostBoy)

def TheLostBoy(character):
    """
    The second event of the story where the character is asked to rescue a boy.
    
    Parameters:
    - character: The player's character.
    """
    theLostBoy = (
        "After a grueling battle, you arrive at Harrenhal, a decaying fortress shrouded in mist. "
        "Its once-mighty walls now crumble, and the people live in fear under oppressive rule. "
        "As you approach the keep, a terrified woman rushes toward you, her clothes tattered and her face pale.\n\n"
        "'Please, help me!' she pleads. 'My little brother has been taken by a soldier, dragged into the keep as a gift for their cruel lord.'\n\n"
        "Will you help her?\n"
        "Type 'yes' or 'no':"
    )
    
    theLostBoyPart2 = (
        "Moved by the woman’s plight, you agree to help her find her brother. "
        "She leads you to the entrance of the keep, where the guards are stationed."
        "They eye you suspiciously but are too intimidated by your presence to interfere.\n\n"
        "The woman, who introduces herself as Liana, explains that the soldiers have been taking children from the nearby villages as offerings to their cruel lord."
        "She fears that her brother is destined for a dark and terrible fate if you do not act quickly.\n\n"
        "You enter the keep, its halls dark and foreboding. The air is thick with the stench of decay, and you can hear the distant cries of those who have suffered within these walls."
        "Liana stays close behind you, her fear palpable as you descend deeper into the bowels of Harrenhal."
        "Suddenly, the soldier appeared in front of you ready for a battle."
    )
    
    theLostBoyPart3 = (
        "With a final, powerful strike, you defeat the soldier, sending him crumpling to the ground."
        "Liana rushes to her brother’s side, tears streaming down her face as she unties his bonds and holds him close.\n\n"
        "“Thank you... thank you so much,” she sobs, overwhelmed with relief and gratitude.\n\n"
        "You have received:\n"
        "Exp: 50\n"
        "Gold: 25 coins"
        "x1 Health Potion"
    )
    
    theLostBoyInput = get_valid_input(theLostBoy, ["yes", "no"])
    log_and_record(theLostBoyInput, is_input=True)
    
    if theLostBoyInput == "yes":
        historyLine(theLostBoyPart2)
        if handle_battle(character, Soldier()):
            historyLine(theLostBoyPart3)
            character.exp += 50
            character.gold += 25
            menuCaller(character, TheElvenEnclave)
            character.add_item("Health Potion")
    elif theLostBoyInput == "no":
        historyLine("\nYou decide not to get involved, leaving the young woman to search for her brother on her own. The young woman is disappointed as you turn away.\n")
        menuCaller(character, TheElvenEnclave)

def TheElvenEnclave(character):
    """
    The third event of the story where the character is asked to help defend the Elven Enclave.
    
    Parameters:
    - character: The player's character.
    """
    arrival = (
        "You journey deep into the ancient forest of Aeloria, where the trees tower above, their leaves shimmering with a faint, ethereal glow. "
        "The air is thick with the scent of pine and moss, and the distant sound of flowing water guides you forward.\n\n"
        "After hours of travel, you arrive at the hidden Elven Enclave, a place of breathtaking beauty and serenity. "
        "Elven structures, crafted from living wood and adorned with silver and crystal, blend seamlessly with the natural surroundings. "
        "The elves here, tall and graceful, move with an elegance that seems almost otherworldly."
    )
    
    pleaForHelp = (
        "As you admire the enclave, a young elf with silver hair and piercing blue eyes approaches you. "
        "His expression is grave, and there is an urgency in his voice as he speaks.\n\n"
        "'Traveler, I am Luthien, a guardian of this enclave. We are in desperate need of your help. "
        "A dark force has begun to corrupt our sacred grove, twisting the spirits of the forest into vile creatures. "
        "Our warriors are holding them at bay, but our strength wanes. Will you aid us in defending our home?'\n\n"
        "Will you help the elves defend their sacred grove?\n"
        "Type 'yes' or 'no':"
    )
    
    defendingTheGrove = (
        "Moved by Luthien’s plea, you agree to help defend the grove. "
        "He leads you to the heart of the enclave, where ancient trees form a natural barrier against the encroaching darkness. "
        "Elven archers are perched in the treetops, their arrows glowing with magical energy.\n\n"
        "As you take your position, the ground trembles, and from the shadows, twisted creatures emerge—once noble forest spirits, now corrupted by dark magic. "
        "Their eyes burn with malevolence as they charge towards the grove, intent on destroying everything in their path.\n\n"
        "You ready your weapon, preparing to face the oncoming horde."
    )
    
    victoryInBattle = (
        "With swift strikes and unwavering resolve, you and the elves repel the dark creatures, cutting them down before they can breach the grove. "
        "The corrupted spirits let out haunting wails as they fall, their forms dissipating into wisps of dark mist.\n\n"
        "As the last of the creatures is defeated, the grove falls silent once more. "
        "Luthien approaches you, his expression one of deep gratitude.\n\n"
        "'You have saved us, traveler. The sacred grove is safe, thanks to your courage and skill. "
        "Please, accept this as a token of our gratitude.'\n\n"
        "You have received:\n"
        "Exp: 100\n"
        "Elven Bow: A finely crafted bow imbued with the magic of the forest."
    )
    
    defeatInBattle = (
        "Despite your best efforts, the dark creatures overwhelm you and the elven defenders. "
        "The sacred grove is breached, and you fall to the ground, your vision fading as the once-beautiful enclave is consumed by darkness."
    )
    
    # Begin the event
    historyLine(arrival)
    theElvenEnclaveInput = get_valid_input(pleaForHelp, ["yes", "no"])
    log_and_record(theElvenEnclaveInput, is_input=True)
    
    if theElvenEnclaveInput == "yes":
        historyLine(defendingTheGrove)
        if handle_battle(character, Elf()):
            historyLine(victoryInBattle)
            character.exp += 100
            character.add_item("Elven Bow")
            endGame(character)
    elif theElvenEnclaveInput == "no":
        historyLine(defeatInBattle)
        endGame(character)