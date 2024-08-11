import os
from datetime import datetime

def fileChecker():
    """
    Check files within the Input directory and move them to the appropriate location.
    
    No Args
    """
    inputDirectory = "Input"  # Define the input directory containing files to check
    destinationDir = "Destination"  # Define the directory to move valid files to
    miscDir = "Misc"  # Define the directory to move invalid files to
    try:
        # Loop through each file in the input directory
        for filename in os.listdir(inputDirectory):
            file_path = os.path.join(inputDirectory, filename)  # Get the full path of the file
            if os.path.isfile(file_path):  # Check if the path is a file
                if fileFormat(filename):  # Check if the file format is correct
                    newFilename = renameFile(filename)  # Rename the file
                    destination_path = os.path.join(destinationDir, newFilename)  # Construct the new path for the file
                    os.rename(file_path, destination_path)  # Move the file to the destination directory
                    print(f"Renamed and moved {filename} to {destination_path}")  # Print confirmation message
                else:
                    misc_path = os.path.join(miscDir, filename)  # Construct the path for the invalid file
                    os.rename(file_path, misc_path)  # Move the file to the misc directory
                    print(f"Moved {filename} to {misc_path}")  # Print confirmation message
    except Exception as e:
        print(f"An error occurred while checking the file: {e}")  # Print error message if something goes wrong

def fileFormat(filename):
    """
    Check if the file name contains a date in the MM-DD-YYYY format.
    
    Args:
        filename (str): The name of the file to check.
    
    Returns:
        bool: True if the date format is correct, False otherwise.
    """
    base_filename, _ = os.path.splitext(filename)  # Get the base name of the file without extension
    
    # Split the base filename by spaces to separate any prefix from the date part
    parts = base_filename.split(' ')
    date_part = parts[-1]  # Get the last part which should be the date
    
    date_parts = date_part.split('-')  # Split the date part by dashes
    if len(date_parts) != 3:  # Check if the date part has exactly 3 components
        return False
    month, day, year = date_parts  # Extract month, day, and year
    if len(day) != 2 or len(month) != 2 or len(year) != 4:  # Check if day and month are 2 digits and year is 4 digits
        return False
    try:
        # Try to create a date with month, day, and year to validate the date
        datetime.strptime(f"{month}-{day}-{year}", "%m-%d-%Y")
        return True
    except ValueError:
        return False  # Return False if the date is invalid

def renameFile(filename):
    """
    Rename the file from MM-DD-YYYY format to YYYY-MM-DD format.
    
    Args:
        filename (str): The name of the file to rename.
    
    Returns:
        str: The new name of the file.
    """
    try:
        base_filename, ext = os.path.splitext(filename)  # Get the base name and extension of the file
        
        # Split the base filename by spaces to separate any prefix from the date part
        parts = base_filename.split(' ')
        date_part = parts[-1]  # Get the last part which should be the date
        month, day, year = date_part.split('-')  # Split the date part by dashes
        
        # Reconstruct the filename with the new date format YYYY-MM-DD
        new_date = f"{year}-{month}-{day}"
        if len(parts) > 1:
            new_base_filename = ' '.join(parts[:-1]) + ' ' + new_date  # Combine prefix with new date
        else:
            new_base_filename = new_date  # No prefix, just the new date
            
        return f"{new_base_filename}{ext}"  # Return the new filename with extension
    except Exception as e:
        print(f"Error renaming the file: {e}")  # Print error message if something goes wrong
        return filename  # Return the original filename if there is an error

