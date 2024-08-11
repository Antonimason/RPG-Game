from Utilities.utilities import recordDocument, historyLine

def battle(character, enemy):
    """
    Initiates and manages the battle between the character and the enemy.
    
    Args:
        character (Player): The player character participating in the battle.
        enemy (Enemy): The enemy character the player is fighting against.
    """
    start_battle(character, enemy)
    
    while character.getCurrentHealth() > 0 and enemy.getCurrentHealth() > 0:
        decision = get_player_action(character, enemy)
        if not handle_action(decision, character, enemy):
            historyLine("\nSorry, input not valid\n")
            continue

        if enemy.getCurrentHealth() > 0:
            enemy_attack(character, enemy)
        
        check_defeat(character, enemy)

def start_battle(character, enemy):
    """
    Displays the initial battle message and shows the current status.
    
    Args:
        character (Player): The player character participating in the battle.
        enemy (Enemy): The enemy character the player is fighting against.
    """
    message = "\nThe battle has started!\n"
    historyLine(message)
    display_battle_status(character, enemy)

def display_battle_status(character, enemy):
    """
    Creates a formatted string showing the current health of the character and enemy,
    and the available actions for the player.
    
    Args:
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    
    Returns:
        str: A string representing the battle status and player options.
    """
    status_message = (
        f"\nYour current Health is: {character.getCurrentHealth()} and your mana is: {character.getCurrentMana()}"
        f"\nyour enemy Health is: {enemy.getCurrentHealth()}\n"
        "\nWhat do you want to do?\n"
        "Type 1 to attack\n"
        "Type 2 to make a special attack\n"
        "Type 3 to defend\n"
        "Type 4 to heal\n"
    )
    return status_message

def get_player_action(character, enemy):
    """
    Prompts the player for their action during the battle and records the input.
    
    Args:
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    
    Returns:
        str: The player's chosen action.
    """
    action = input(display_battle_status(character, enemy))
    recordDocument(action)
    return action

def handle_action(decision, character, enemy):
    """
    Executes the action based on the player's decision.
    
    Args:
        decision (str): The player's action choice (e.g., "1" for attack).
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    
    Returns:
        bool: True if the action was handled successfully, False otherwise.
    """
    if decision == "1":
        perform_attack(character, enemy)
    elif decision == "2":
        perform_special_attack(character, enemy)
    elif decision == "3":
        perform_defense(character, enemy)
    elif decision == "4":
        perform_heal(character)
    else:
        return False
    return True

def perform_attack(character, enemy):
    """
    Executes a regular attack from the character to the enemy.
    
    Args:
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    """
    damage = character.performAttack()
    enemy.currentHealth -= damage
    historyLine(f"\nYou attacked the {enemy.getName()} for {damage} damage!\n")

def perform_special_attack(character, enemy):
    """
    Executes a special attack from the character to the enemy.
    
    Args:
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    """
    special_damage = character.getSpecialAttackDamage()
    if(special_damage == None):
        historyLine(f"Sorry, your current mana is: {character.getCurrentMana()} and it is too low")
    else:
        enemy.currentHealth -= special_damage
        historyLine(f"\nYou used a special attack on the {enemy.getName()} for {special_damage} damage!\n")

def perform_defense(character, enemy):
    """
    Executes a defense action for the character against the enemy's attack.
    
    Args:
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    """
    defense = character.getDefense()
    enemy_attack = enemy.performAttack() - defense
    enemy_attack = max(0, enemy_attack)  # Ensure that damage cannot be negative
    character.currentHealth -= enemy_attack
    historyLine(f"\nYou defended against the {enemy.getName()}'s attack, reducing damage to {enemy_attack}!\n")

def perform_heal(character):
    """
    Heals the character and updates their health.
    
    Args:
        character (Player): The player character.
    """
    healing = character.heal()
    # Ensure that health does not exceed maximum health
    if character.currentHealth > character.getMaxHealth():
        character.currentHealth = character.getMaxHealth()
    historyLine(f"\nYou healed yourself for {healing} health!\n")

def enemy_attack(character, enemy):
    """
    Executes an attack from the enemy to the character.
    
    Args:
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    """
    enemy_damage = enemy.performAttack()
    character.currentHealth -= enemy_damage
    historyLine(f"\nThe {enemy.getName()} attacked you for {enemy_damage} damage!\n")

def check_defeat(character, enemy):
    """
    Checks if either the character or the enemy has been defeated.
    
    Args:
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    """
    if character.getCurrentHealth() <= 0:
        historyLine("\nYou have been defeated!\n")
        character.isAlive = False

    if enemy.getCurrentHealth() <= 0:
        historyLine(f"\nThe {enemy.getName()} has been defeated!\n")
        reward(character,enemy)

def reward(character,enemy):
    """
    Obtaining a reward once the enemy is defeated
    
    Args:
        character (Player): The player character.
        enemy (Enemy): The enemy character.
    """
    
    #getting enemy rewards stats
    goldRewarded = enemy.getGold()
    expRewarded = enemy.getExp()
    historyLine(f"\nYour reward:\n Experience: {expRewarded}.\n Gold: {goldRewarded} coins.\n")
    
    # Adding reward to character and restarting character current health and mana
    character.gold += goldRewarded
    character.setExp(expRewarded)
    character.currentHealth = character.maxHealth
    character.currentMana = character.maxMana
    
