from pathlib import Path
from os import listdir
from os.path import isfile, join
from pydantic import BaseModel
import uvicorn
import os
from typing import Optional
from fastapi import FastAPI, File, UploadFile
from api.src.files import convert_to_string, return_string, upload_new_file, return_files
from api.src.joke import read_json, get_joke, insert_joke, delete_joke_by


app = FastAPI()


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
    return {"Hello": "World"}


@app.post('/files/check_content_json')
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    json_string = convert_to_string(content)
    return {'file_contents': json_string}


@app.post("/files/upload")
def create_file(file: UploadFile = File(...)):
    return upload_new_file(file)


@app.get('/files/savefolder')
def check_save_folder():
    return return_files()


@app.get('/files/savefolder/')
def read_file_from_save(file_id: int = 0):
    data = return_string(file_id)
    return data


@app.get('/jokes/alljokes')
def get_all_jokes():
    return read_json()


@app.get('/jokes/')
def return_specific_joke(joke_id: int = 0):
    return get_joke(joke_id)


@app.post('/jokes/insert/')
def input_joke(joke: Joke):
    return insert_joke(joke)


@app.post('/jokes/delete/')
def delete_joke(joke_id: int):
    return delete_joke_by(joke_id)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')
