from Utilities.utilities import historyLine
def characterStats(character):
    stats = (
        f"\n|-------------------- Character Stats ---------------------|\n"
        f"| Name: {character.getName()}               \n"
        f"| Gender: {character.getGender()}               \n"
        f"| Profession: {character.getProfession()}        \n"
        f"| Level: {character.getLevel()}                  \n"
        f"| Exp: {character.getExp()}                      \n"
        f"| Gold: {character.getGold()}                    \n"
        f"|-------------------- Attributes ---------------------|\n"
        f"| Max Health: {character.getMaxHealth()}         \n"
        f"| Current Health: {character.getCurrentHealth()} \n"
        f"| Max Mana: {character.getCurrentHealth()}       \n"
        f"| Current Mana: {character.getCurrentMana()}     \n"
        f"| Attack: {character.getAttack()}                \n"
        f"| Special Attack: {character.getSpecialAttack()} \n"
        f"| Defense: {character.getDefense()}              \n"
        f"| Healing: {character.getHealing()}              \n"
        "|------------------------------------------------|\n"
    )
    historyLine(stats)