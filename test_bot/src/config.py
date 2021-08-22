import json

API_KEY = 'None'
API_SECRET = 'None'

SECRET_FILE = "test_bot/.secrets/.api-secrets.json" #path to the secret file

def get_api_key():
    try:
        with open(SECRET_FILE, 'r') as read_file:
            data = json.load(read_file)
            API_KEY = data['api']
    except IOError:
        print("INPUT ERROR: File with api secrets doesn't exist")

    else:
        return API_KEY

def get_api_secret():
    try:
        with open(SECRET_FILE, 'r') as read_file:
            data = json.load(read_file)
            API_SECRET = data['secret']
    except IOError:
        print("INPUT ERROR: File with api secrets doesn't exist")

    else:
        return API_SECRET

get_api_key()