from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import datetime
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Replace with your credentials file path and document ID
CREDENTIALS_FILE = resource_path('data/token.json')
DOCUMENT_ID = '1dp3IVZ2pvxJQTdXsj34B7im6LT1GzEs1LebGYXxg8Z8'

# Replace with your date range
# START_DATE = '2023-07-26'
# END_DATE = '2023-08-3'



def authenticate():
    credentials = Credentials.from_authorized_user_file(CREDENTIALS_FILE)
    service = build('docs', 'v1', credentials=credentials)
    return service

def get_document_content(service, document_id):
    document = service.documents().get(documentId=document_id).execute()
    return document.get('body', {}).get('content', [])

def extract_logs(content,startDate,endDate,action):
    logs = []
    current_date = None
    for element in content:
        if 'paragraph' in element:
            paragraph = element['paragraph']
            text = ''.join(run['textRun']['content'] for run in paragraph['elements'])
            date_time_str = text[1:11]
            # Check if the line contains date and time
            if date_time_str[5:7] < endDate[5:7]:
                    if action != "All Actions":
                        if text.startswith('[')and text.find(action.upper()) !=-1:
                            if (date_time_str[5:7] == startDate[5:7]) and (date_time_str[8:10] >= startDate[8:10]):
                                logs.append(text)
                    elif action == "All Actions":
                        if text.startswith('['):
                            date_time_str = text[1:11]
                            if (date_time_str[5:7] == startDate[5:7]) and (date_time_str[8:10] >= startDate[8:10]):
                                logs.append(text)
            elif date_time_str[5:7] == endDate[5:7]:
                    if startDate[5:7] == endDate[5:7]:
                        if date_time_str[8:10] <= endDate[8:10]:    
                            if action != "All Actions":
                                if text.startswith('[')and text.find(action.upper()) !=-1:
                                    if (date_time_str[8:10] >= startDate[8:10]) and (date_time_str[8:10] <= endDate[8:10]):
                                        logs.append(text)
                            elif action == "All Actions":
                                if text.startswith('['):
                                    date_time_str = text[1:11]
                                    if (date_time_str[8:10] >= startDate[8:10]) and (date_time_str[8:10] <= endDate[8:10]):
                                        logs.append(text)
                    else:
                        if date_time_str[8:10] <= endDate[8:10]:    
                            if action != "All Actions":
                                if text.startswith('[')and text.find(action.upper()) !=-1:
                                    if (date_time_str[8:10] <= endDate[8:10]):
                                        logs.append(text)
                            elif action == "All Actions":
                                if text.startswith('['):
                                    date_time_str = text[1:11]
                                    if (date_time_str[8:10] <= endDate[8:10]):
                                        logs.append(text)

    return logs

# START_DATE = '2023-07-26'
# END_DATE = '2023-08-3'


def main():
    service = authenticate()
    content = get_document_content(service, DOCUMENT_ID)
    return content

if __name__ == "__main__":
    main()
