import os
import shutil
from pathlib import Path
from os import listdir
from os.path import isfile, join
from pydantic import BaseModel

from typing import Optional
from fastapi import FastAPI, File, UploadFile
from create_data import convert_to_string, return_string
from joke import read_json, get_joke, insert_joke, delete_joke_by


app = FastAPI()
cwd_path = Path('../save_folder')

class Joke(BaseModel):
    text: str
    question: str
    answer: str
    author: str
    created: str
    tags: Optional[list] = None
    rating: int


@app.get("/")
def read_root():
    return {"Ukázková stránka"}

@app.get("/hello")
def read_hello():
    return {"Hello": "World"}

@app.post('/files/check_content_json')
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    json_string = convert_to_string(content)
    return {'file_contents': json_string}
    
@app.post("/files/upload")
def create_file(file: UploadFile = File(...)):
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

@app.get('/files/savefolder')
def check_save_folder():
    onlyfiles = [f for f in listdir(cwd_path) if isfile(join(cwd_path, f))]
    return onlyfiles

@app.get('/files/savefolder/')
def read_file_from_save(id: int = 0):
    data = return_string(id)
    return data

@app.get('/jokes/alljokes')
def get_all_jokes():
    return read_json()

@app.get('/jokes/')
def return_specific_joke(id: int = 0):
    return get_joke(id)

@app.post('/jokes/insert/')
def input_joke(joke: Joke):
    return insert_joke(joke)

@app.post('/jokes/delete/')
def delete_joke(id: int):
    return delete_joke_by(id)