# Note 1: this project use Python 2.7
# Note 2: this project export data to Google Sheets API v4
# Note 3: this project named TRpermission means Track Revenue permissions assignment.

import httplib2
import os
import json
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

class Assignment:
    # get the credentials
    def get_credentials(self):
        SCOPES = 'https://www.googleapis.com/auth/drive'
        CLIENT_SECRET_FILE = 'client_secret.json'
        APPLICATION_NAME = 'TRpermissions'

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


    def main(self, body):
        credentials = self.get_credentials()
        http = credentials.authorize(httplib2.Http())
        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                        'version=v4')
        service = discovery.build('sheets', 'v4', http=http,
                                  discoveryServiceUrl=discoveryUrl)

        spreadsheet_body = {'properties': {'title': "TRpermissions"}}
        request = service.spreadsheets().create(body=spreadsheet_body)
        response = request.execute()
        # here the spreadsheet Url will be printed, pls check the sheet in this URL
        print response
        spreadsheetId = response['spreadsheetId']
        response = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetId, body=body).execute()
        print response


    # load data from json source
    def load(self):
        with open('original.json') as json_file:
            dict = json.load(json_file)
            return dict
    # import the right data to the sheet
    def import_data(self, data_need):
        # create array store the aim data
        array = []
        permission = [' ', 'view_grades', 'change_grades', 'add_grades', 'delete_grades', 'view_classes', 'change_classes', 'add_classes', 'delete_classes']
        array.append(permission)
        # in order of the user name
        data = sorted(data_need.items(), key=lambda x: x[0])
        for key,value in data:
            line = ['0' for i in range(len(permission))]
            line[0] = key
            for ele in value:
                if ele in permission:
                    id = permission.index(ele)
                    line[id] = '1'
            array.append(line)
        # check if array is None
        try:
            array[0]
        except IndexError:
            print 'Careful: No data in array'
            raise
        # import to sheet
        row = len(array)
        col = len(array[0])
        body = {'requests':
                    [{'appendCells':
                          {'fields': '*', 'rows': [],
                           'sheetId': 0}}]}
        for i in range(row):
            body['requests'][0]['appendCells']['rows'].append({'values':[]})
            for j in range(col):
                body['requests'][0]['appendCells']['rows'][-1]['values'].append({'userEnteredValue':
                                                                    {'stringValue': array[i][j]},
                                                                'userEnteredFormat': {
                                                                    'backgroundColor': {'blue': 0.8,
                                                                                        'alpha': 0.5,
                                                                                        'green': 0.8,
                                                                                        'red': 0.8}}})
        return body

if __name__ == '__main__':
# Before import data, I assume I have a json file in the direction. So I made up one use below code.
    original = {"student1": ["view_grades", "view_classes"],
            "student2": ["view_grades", "view_classes"],
            "teacher": ["view_grades", "change_grades", "add_grades", "delete_grades","view_classes"],
            "principle": ["view_grades", "view_classes", "change_classes", "add_classes", "delete_classes"]}
    with open("original.json", "w") as f:
        json.dump(original, f)
    # import data start here
    one = Assignment()
    data_need = one.load()
    body = one.import_data(data_need)
    one.main(body)
