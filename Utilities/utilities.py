import re

def historyLine(text):
    print(text)
    # IMPORTANT
    #agregar un loop para meter toda la informacion del juego en un array para cuando termine el juego se envie de manera ordenada a recordDocument
    recordDocument(text)
    
def recordDocument(text):
    with open("copy.txt", "a") as file:
        file.write(text)  

def fileOrganizerCaller():
    pass