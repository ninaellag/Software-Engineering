import json


def write_to_config(username, client_id, client_secret, redirect_uri, filename):
    config = {'username': username, 'client_id': client_id, 'client_secret': client_secret,
              'redirect_uri': redirect_uri}
    with open(filename, 'w') as fp:
        json.dump(config, fp)
