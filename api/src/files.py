import pandas as pd
import json
import os
import shutil
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

def upload_new_file(file):
    # Save file on disk 
    # Great debate on how to do it without much loss of frames on link below:
    # https://github.com/tiangolo/fastapi/issues/426
    # reading file for return contents of the file
    upload_folder = cwd_path
    file_object = file.file
    #create empty file to copy the file_object to
    upload_folder = open(os.path.join(upload_folder, file.filename), 'wb+')
    shutil.copyfileobj(file_object, upload_folder)
    upload_folder.close()
    return {"filename": file.filename}


# Function for return string from file
def return_string(id):
    onlyfiles = [f for f in listdir(cwd_path) if isfile(join(cwd_path, f))]
    file = onlyfiles[id]

    fullPath = str(cwd_path) + '/' + file

    with open (fullPath) as file:
        data = file.read()
    return data