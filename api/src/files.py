import pandas as pd
import json
from os import listdir
from os.path import isfile, join
from pathlib import Path

cwd_path = Path('../save_folder/')

# Function for reading json
def convert_to_string(bytes):
    data = bytes.decode('utf-8').splitlines()
    df = pd.DataFrame(data)
    return parse_csv(df)

def parse_csv(df):
    result = df.to_json(orient='records')
    parsed = json.loads(result)
    return parsed

# Function for return string from file
def return_string(id):
    onlyfiles = [f for f in listdir(cwd_path) if isfile(join(cwd_path, f))]
    file = onlyfiles[id]

    fullPath = str(cwd_path) + '/' + file

    with open (fullPath) as file:
        data = file.read()
    return data