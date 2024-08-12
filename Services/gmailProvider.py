import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv, find_dotenv
import base64
import mimetypes
from email.message import EmailMessage

 #Code extracted from GoogleCloudPlatform   
def get_creds():
    
    #Searching for our .env file
    dotenv_path = find_dotenv()
    # Loading .env file
    load_dotenv(dotenv_path)
    #getting our variable from .env file
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    
    creds = None
    
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        print("Have tokens!")
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print("Refreshed token!")
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
            print("Got new token")
    # Save the credentials for the next run
    with open("token.json", "w") as token:
          token.write(creds.to_json())
    return creds

def gmail_send_message(messageContent, subject, recipient, file):
      """Create and send an email message
      Print the returned  message id
      Returns: Message object, including message id
    
      Load pre-authorized user credentials from the environment.
      TODO(developer) - See https://developers.google.com/identity
      for guides on implementing OAuth2 for the application.
      """
      creds = get_creds()

      try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()
    
        message.set_content(messageContent)
    
        message["To"] = recipient
        message["From"] = "sba23108@student.cct.ie"
        message["Subject"] = subject
        
        if file:
            attachment_filename = file
            ctype, encoding = mimetypes.guess_type(attachment_filename)
            if ctype is None or encoding is not None:
                ctype = 'application/octet-stream'
            maintype, subtype = ctype.split('/', 1)

            with open(attachment_filename, 'rb') as fp:
                message.add_attachment(fp.read(),
                                    maintype=maintype,
                                    subtype=subtype,
                                    filename=os.path.basename(attachment_filename))
    
        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    
        create_message = {"raw": encoded_message}
        # pylint: disable=E1101
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
      except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
      return send_message

