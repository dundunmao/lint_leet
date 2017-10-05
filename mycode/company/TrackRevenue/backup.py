import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheet_body = {'properties': {'title': "324"}}
    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    print response

    spreadsheetId = response['spreadsheetId']
    body = {'requests':
                [{'appendCells':
                      {'fields': '*', 'rows': [{'values': [{'userEnteredValue':
                                                                {'stringValue': '1'},
                                                            'userEnteredFormat': {
                                                                'backgroundColor': {'blue': 0.8,
                                                                                    'alpha': 0.5,
                                                                                    'green': 0.8,
                                                                                    'red': 0.8}}},
                                                           {'userEnteredValue': {'stringValue': '2'},
                                                            'userEnteredFormat': {
                                                                'backgroundColor': {'blue': 0.8,
                                                                                    'alpha': 0.5,
                                                                                    'green': 0.8,
                                                                                    'red': 0.8}}}]
                                                },
                                               {'values': [{'userEnteredValue': {'stringValue': '3'},
                                                            'userEnteredFormat': {
                                                                'backgroundColor': {'blue': 0.8,
                                                                                    'alpha': 0.5,
                                                                                    'green': 0.8,
                                                                                    'red': 0.8}}},
                                                           {'userEnteredValue': {'stringValue': '4'},
                                                            'userEnteredFormat': {
                                                                'backgroundColor': {'blue': 0.8,
                                                                                    'alpha': 0.5,
                                                                                    'green': 0.8,
                                                                                    'red': 0.8}}}]
                                                }
                                               ],
                       'sheetId': 0}}]}
    response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId, body=body).execute()
    print response


if __name__ == '__main__':
    main()
