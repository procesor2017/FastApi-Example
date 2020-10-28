import json
from json import JSONEncoder
from os import listdir
from os.path import isfile, join
from pathlib import Path
from collections import OrderedDict

cwd_path = Path('api/json/jokes.json') # For uvicorn
# cwd_path = Path('api/json/jokes.json') # For creating

def read_json():
    # Read json file
    with open (cwd_path, 'r') as file:
        data = json.load(file)
        return data

def get_joke(id):
    with open (cwd_path, 'r') as file:
        data = json.load(file)
        return data[id]

# Insret joke to db #################################################
'''
Bcs old python in 3.5+ using just jsons
'''

def insert_joke(body):
    with open (cwd_path) as json_file:
        data = json.load(json_file)

        add_data = OrderedDict(body)
        add_data['id'] = len(data)
        add_data.move_to_end('id', last = False)

        data.append(add_data) 


    with open(cwd_path,'w') as f: 
        json.dump(data, f, indent=4, cls=MyEncoder)
    return 'Joke was inserted under id: ' + str(len(data)-1 )
        
class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def delete_joke_by(id):
    i = 0
    with open (cwd_path, 'r') as file:
        data = json.load(file)
        while i < len(data):
            if data[i]['id'] == id:
                del data[i]
            i += 1
    
    with open(cwd_path, 'w') as new_json:
        json.dump(data, new_json, indent=4)
    return 'Joke id: ' + str(id) + ' was deleted' 
