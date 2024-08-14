import os
from datetime import datetime

def historyLine(text):
    """
    Prints the provided text and records it in the document.

    Args:
        text (str): The text to be printed and recorded.
    """
    print(text)
    recordDocument(text)

def recordDocument(text):
    """
    Records the provided text into the appropriate file.
    If the file already exists, it appends the text to the file.

    Args:
        text (str): The text to be recorded in the file.
    """
    # Define the output file name
    fileName = getFile()
    with open(fileName, "a") as file:
        # If the file already contains content, start a new line before appending
        if file.tell() > 0:
            file.write("\n")
        # Write the text to the file
        file.write(text)

def getDocumentOnlyRead():
    """
    Reads and returns the content of the document for today.

    Returns:
        str: The content of today's document.
    """
    fileName = getFile()
    return open("Input/" + fileName, "r").read()

def count_lines_in_file(fileName):
    """
    Counts the number of lines in a specified file.

    Args:
        fileName (str): The name of the file to count lines in.

    Returns:
        int: The number of lines in the file. If the file is not found, returns 0.
    """
    try:
        with open("Input/" + fileName, "r") as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0    

def getFile():
    """
    Generates the filename for today's story document based on the current date.

    Returns:
        str: The filename formatted as "Input/story MM-DD-YYYY.txt".
    """
    # Get today's date
    today = datetime.today()
    day = today.day
    month = today.month
    year = today.year
    # Format the date as MM-DD-YYYY
    date = datetime.strptime(f"{month}-{day}-{year}", "%m-%d-%Y")
    formatted_date = date.strftime("%m-%d-%Y")
    
    # Define the output file name
    fileName = f"Input/story {formatted_date}.txt"
    
    return fileName
