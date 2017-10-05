# -*- encoding: utf-8 -*-
# https://developers.google.com/sheets/api/reference/rest/v4/spreadsheets/create/
from collections import OrderedDict
import json
from collections import OrderedDict
from pprint import pprint

from googleapiclient import discovery





# from __future__ import print_function
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

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'original.json'
APPLICATION_NAME = 'TRpermissons'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, 'linshi/TrackRevenue')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-TRpermissons.json')

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

#
#
# def store(da):
#     array = par_data(da)
#     with open('information.csv', 'w') as file_line:
#         for l in array:
#             file_line.write(l)
#
#
def load():
    with open('original.json') as json_file:
        dict = json.load(json_file)
        return dict

def par_data(da):
    array = []
    permission = ['        ', 'view_grades', 'change_grades', 'add_grades', 'delete_grades', 'view_classes', 'change_classes', 'add_classes', 'delete_classes']
    array.append(permission)
    for key,value in da.items():
        line = [0 for i in range(len(permission))]
        line[0] = key
        for ele in value:
            if ele in permission:
                id = permission.index(ele)
                line[id] = 1
        array.append(line)
    # return array
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    data = {'properties': {'title': 'My new Sheet'}}
    sheet = service.spreadsheets().create(body=data).execute()

# def create():
#     credentials = None
#
#     service = discovery.build('sheets', 'v4', credentials=credentials)
#
#     spreadsheet_body = {
#         # TODO: Add desired entries to the request body.
#     }
#
#     request = service.spreadsheets().create(body=spreadsheet_body)
#     response = request.execute()
#
#     # TODO: Change code below to process the `response` dict:
#     pprint(response)

if __name__ == "__main__":

    # original = {"student1": ["view_grades", "view_classes"],
    #         "student2": ["view_grades", "view_classes"],
    #         "teacher": ["view_grades", "change_grades", "add_grades", "delete_grades","view_classes"],
    #         "principle": ["view_grades", "view_classes", "change_classes", "add_classes", "delete_classes"]}
    # with open("original.json", "w") as f:
    #     json.dump(original, f)
    l = []
    try:
        l[0]
    except IndexError:
        print 'None'
    # print par_data(load())

