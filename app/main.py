from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Bienvenue sur la Masterclass Devops chez  Datascientest"}

