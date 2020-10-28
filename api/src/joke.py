import json
import os
from json import JSONEncoder
from pathlib import Path
from collections import OrderedDict

# For uvicorn
local_path = Path('json/jokes.json')

# For heroku / local
cloud_path = Path('api/json/jokes.json')


def choose_path():
    if os.path.exists(local_path):
        return local_path
    else:
        return cloud_path


def read_json():
    # Read json file
    cwd_path = choose_path()
    with open(cwd_path, 'r') as file:
        data = json.load(file)
        return data


def get_joke(joke_id):
    cwd_path = choose_path()
    with open(cwd_path, 'r') as file:
        data = json.load(file)
        return data[joke_id]


# Insret joke to db #################################################
'''
Bcs old python in 3.5+ using just jsons
'''


def insert_joke(body):
    cwd_path = choose_path()
    with open(cwd_path) as json_file:
        data = json.load(json_file)

        add_data = OrderedDict(body)
        add_data['id'] = len(data)
        add_data.move_to_end('id', last=False)

        data.append(add_data)

    with open(cwd_path, 'w') as f:
        json.dump(data, f, indent=4, cls=MyEncoder)
    return 'Joke was inserted under id: ' + str(len(data) - 1)


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def delete_joke_by(joke_id):
    cwd_path = choose_path()
    i = 0
    with open(cwd_path, 'r') as file:
        data = json.load(file)
        while i < len(data):
            if data[i]['id'] == joke_id:
                del data[i]
            i += 1

    with open(cwd_path, 'w') as new_json:
        json.dump(data, new_json, indent=4)
    return 'Joke id: ' + str(id) + ' was deleted'
