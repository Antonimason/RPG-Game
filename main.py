import os;
from Chapters.characterCreation import characterCreation


def main():

    #Directories name
    folders = ["Misc", "Input", "Destination"]

    #If they do not exist then the system create them
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Directory '{folder}' has been created.")
        else:
            print(f"Directory '{folder}' already exists.")

    #Starting character creation process
    characterCreation()
    
if __name__ == "__main__":
    main()
