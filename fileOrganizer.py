#For this part, you are required to develop a Python program that:
#Takes in an input directory, a destination directory, and a misc directory as inputs. 
#Renames all files in the input directory, so that instead of month/day/year the file name goes year/month/day.
#Moves the renamed files to the destination directory
#Any file that is not renamed is instead moved to the misc directory.

import os  # Import the 'os' module to interact with the file system
from datetime import datetime  # Import 'datetime' for working with dates

def main():
    """
    Main function to set up directories and initiate the file checking process.
    """
    # Define the input, destination, and misc directories
    inputDirectory = "input"
    destinationDirectory = "destination"
    miscDirectory = "misc"
    
    # Create directories if they don't exist
    createDirectory(inputDirectory)
    createDirectory(destinationDirectory)
    createDirectory(miscDirectory)
    
    trigger = False  # Initialize the trigger to control the loop
    while not trigger:
        # Prompt the user to place documents in the input directory
        checker = input("Please introduce all of your documents into inputDirectory in order to check them all || Have you introduced your documents? Press 'y' or 'n'")
        if checker.lower() == "y":
            # Call the fileChecker function to process the files
            fileChecker(inputDirectory, destinationDirectory, miscDirectory)

def createDirectory(directory):
    """
    Create a directory if it doesn't exist.
    
    Args:
        directory (str): The name of the directory to create.
    """
    try:
        os.mkdir(directory)
        print(f"Directory {directory} has been created.")
    except FileExistsError:
        print(f"Directory {directory} already exists.")
    pass

def fileChecker(directory, destinationDir, miscDir):
    """
    Check files in the given directory and move them to the appropriate location.
    
    Args:
        directory (str): The directory to check files in.
        destinationDir (str): The directory to move valid files to.
        miscDir (str): The directory to move invalid files to.
    """
    try:
        for filename in os.listdir(directory):  # List all files in the input directory
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):  # Check if the path is a file
                if fileFormat(filename):  # Check if the file format is correct
                    newFilename = renameFile(filename)  # Rename the file
                    destination_path = os.path.join(destinationDir, newFilename)
                    os.rename(file_path, destination_path)  # Move the file to the destination directory
                    print(f"Renamed and moved {filename} to {destination_path}")
                else:
                    misc_path = os.path.join(miscDir, filename)
                    os.rename(file_path, misc_path)  # Move the file to the misc directory
                    print(f"Moved {filename} to {misc_path}")
    except Exception as e:
        print(f"An error occurred while checking the file: {e}")

def fileFormat(filename):
    """
    Check if the file name is in the correct format (MM-DD-YYYY).
    
    Args:
        filename (str): The name of the file to check.
    
    Returns:
        bool: True if the format is correct, False otherwise.
    """
    base_filename, _ = os.path.splitext(filename)
    parts = base_filename.split('-')
    if len(parts) != 3:
        return False
    month, day, year = parts
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return True
    try:
        # Try to create a date with month, day, year.
        datetime.strptime(f"{month}-{day}-{year}", "%m-%d-%Y")
        return True
    except ValueError:
        return False

def renameFile(filename):
    """
    Rename the file from MM-DD-YYYY to YYYY-MM-DD format.
    
    Args:
        filename (str): The name of the file to rename.
    
    Returns:
        str: The new name of the file.
    """
    try:
        base_filename, ext = os.path.splitext(filename)
        month, day, year = base_filename.split('-')
        return f"{year}-{month}-{day}{ext}"
    except Exception as e:
        print(f"Error when renaming the file: {e}")
        return filename

if __name__ == "__main__":
    main()

