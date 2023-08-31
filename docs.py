from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
import os
import sys

#create token
# Your Google Docs API scopes (modify as needed)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def authenticate_google_docs():
    SCOPES = ['https://www.googleapis.com/auth/drive']

    creds = None
    # Load or create credentials
    if os.path.exists(resource_path('data/token.json')):
        creds = Credentials.from_authorized_user_file(resource_path('data/token.json'), SCOPES)
        if creds.expired:
            creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(resource_path('data/credentials.json'), SCOPES)
        creds = flow.run_local_server(port=0)

    # Save the credentials for future use
    with open(resource_path('data/token.json'), 'w') as creds_file:
        creds_file.write(creds.to_json())

    return creds

def main():
    creds = authenticate_google_docs()
    service = build('docs', 'v1', credentials=creds)
if __name__ == "__main__":
    main()

authenticate_google_docs()



def read_google_doc(document_id):
    creds = authenticate_google_docs()
    service = build('docs', 'v1', credentials=creds)

    doc = service.documents().get(documentId=document_id).execute()
    content = ""

    for content_element in doc.get('body').get('content'):
        if 'paragraph' in content_element:
            paragraph = content_element['paragraph']
            for element in paragraph['elements']:
                content += element['textRun']['content']

    return content

document_id = '1dp3IVZ2pvxJQTdXsj34B7im6LT1GzEs1LebGYXxg8Z8'

def append_text_to_google_doc(document_id, text_to_append):
    creds = authenticate_google_docs()
    service = build('docs', 'v1', credentials=creds)

    doc = service.documents().get(documentId=document_id).execute()
    doc_content = doc.get('body').get('content')
    start_index = 1
    requests = [
        {
            'insertText': {
                'location': {
                    'index': start_index,
                },
                'text': text_to_append + '\n'
            }
        }
    ]
    result = service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()

    return result




