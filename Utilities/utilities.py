import os
from datetime import datetime

def historyLine(text):
    print(text)
    recordDocument(text)
    
def recordDocument(text):
    # Define el nombre del archivo de salida
    fileName = getFile()
    with open(fileName, "a") as file:
        
        if file.tell() > 0:
            file.write("\n")
        file.write(text)

def getDocumentOnlyRead():
    fileName = getFile()
    return open("Input/" + fileName, "r").read()
    
def count_lines_in_file(fileName):
    try:
        with open("Input/" + fileName, "r") as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0    

def getFile():
    today = datetime.today()
    day = today.day
    month = today.month
    year = today.year
    date = datetime.strptime(f"{month}-{day}-{year}", "%m-%d-%Y")
    formatted_date = date.strftime("%m-%d-%Y")
    
    # Define el nombre del archivo de salida
    fileName = f"Input/story {formatted_date}.txt"
    
    return fileName