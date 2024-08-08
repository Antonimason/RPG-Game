import re

def emailChecker(email):
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    emailMatcher = re.match(email_regex, email)
    # If the email matches the regex, it is valid and return True, otherwise it will return False
    if emailMatcher:
        return True
    return False

def recordDocument(text):
    with open("copy.txt", "a") as file:
        file.write(text)  
        
def gmailProviderCaller():
    pass

def fileOrganizerCaller():
    pass