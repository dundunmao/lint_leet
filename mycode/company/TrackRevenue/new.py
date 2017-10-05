from __future__ import print_function
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



class API:
    def __init__(self, credentials):
        self._credentials = credentials

    def build(self, service, version):
        return discovery.build(service, version, credentials=self._credentials)

    def get_api_kwargs(self):
        return {
            'credentials': self._credentials,
        }


class Spreadsheet(API):
    def __init__(self, info, **kwargs):
        self._info = info
        super(Spreadsheet, self).__init__(**kwargs)

    @property
    def id(self):
        return self._info['spreadsheetId']

    @property
    def permissions(self):
        permissions = self._get_permissions()
        anyone = None
        writers = []
        readers = []
        for x in permissions:
            type = x['type']  #: 'user', 'anyone', 'group', 'domain'
            role = x['role']  #: 'owner', 'commenter', 'reader', 'writer'
            if type == 'anyone':
                if role in ['owner', 'writer']:
                    anyone = 'write'
                elif role in ['reader']:
                    anyone = 'read'
                elif role in ['commenter']:
                    anyone = 'comment'
            elif type == 'user':
                x = self._get_permission(x['id'])
                if role in ['owner', 'writer']:
                    lst = writers
                elif role in ['reader', 'commenter']:
                    lst = readers
                else:
                    raise RuntimeError('Protocol role unknown!')
                lst.append(x['emailAddress'])
        return {
            'anyone': anyone,
            'writers': writers,
            'readers': readers,
        }

    def set_permissions(self, anyone=None, writers=None, readers=None):
        assert anyone in [None, 'writer', 'write',
                          'reader', 'read', 'w', 'r'], 'not in ["r", "w"]'

        drive = self.build('drive', 'v3')
        if anyone:
            role = {
                'r': 'reader',
                'read': 'reader',
                'reader': 'reader',
                'w': 'writer',
                'write': 'writer',
                'writer': 'writer',
            }
            body = {
                'role': role[anyone],
                'type': 'anyone',
            }
            drive.permissions().create(fileId=self.id, body=body).execute()
        if writers:
            body = {
                'role': 'writer',
                'type': 'user',
                'emailAddress': writers,
            }
            drive.permissions().create(fileId=self.id, body=body).execute()
        if readers:
            body = {
                'role': 'reader',
                'type': 'user',
                'emailAddress': readers,
            }
            drive.permissions().create(fileId=self.id, body=body).execute()

    def _get_permissions(self):
        drive = self.build('drive', 'v3')
        r = drive.permissions().list(fileId=self.id).execute()
        permissions = r.get('permissions', [])
        return permissions

    def _get_permission(self, id):
        drive = self.build('drive', 'v3')
        fields = 'allowFileDiscovery,displayName,domain,emailAddress,' \
                 'expirationTime,id,kind,photoLink,role,type'
        permission = drive.permissions().get(
            fileId=self.id, permissionId=id, fields=fields)
        return permission.execute()

    def append(self, data, gray=False, sheet=0):
        spreadsheets = self.build('sheets', 'v4').spreadsheets()
        value = lambda x: {  # noqa
            "userEnteredValue": {"stringValue": str(x)},
            "userEnteredFormat": {"backgroundColor": {
                "red": 0.8, "green": 0.8, "blue": 0.8, "alpha": 0.5}
            }
        } if gray else {
            "userEnteredValue": {"stringValue": str(x)}
        }

        rows = [{"values": [value(cell) for cell in row]} for row in data]
        body = {
            "requests": [
                {
                    "appendCells": {
                        "sheetId": sheet,
                        "rows": rows,
                        "fields": "*",
                    }
                }
            ],
        }

        return spreadsheets.batchUpdate(spreadsheetId=self.id, body=body) \
            .execute()

    def __str__(self):
        return "Sheet(%s)" % self.id



class Spreadsheets(API):
    def create(self, title, anyone=None, writers=None, readers=None):
        assert anyone in [None, 'write', 'read', 'comment', 'w', 'r', 'c'], \
            'not in ["r", "w", "c"]'
        sheets = self.build('sheets', 'v4')
        body = {'properties': {'title': title}}
        res = sheets.spreadsheets().create(body=body).execute()
        spreadsheer = Spreadsheet(res, **self.get_api_kwargs())
        spreadsheer.set_permissions(anyone=anyone, writers=writers,
                                    readers=readers)
        return spreadsheer

    def get(self, id):
        sheets = self.build('sheets', 'v4')
        res = sheets.spreadsheets().get(spreadsheetId=id).execute()
        return Spreadsheet(res, **self.get_api_kwargs())

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
# SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
SCOPES = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets']
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
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
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials



def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)


    api = Spreadsheets(credentials=credentials)
    sheet = api.create('test1', writers=['dundunmao@gmail.com'])
    spreadsheetId = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
    rangeName = 'Class Data!A2:E'
    result = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))


if __name__ == '__main__':
    main()