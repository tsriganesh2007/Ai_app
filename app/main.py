from fastapi import FastAPI
from pydantic import BaseModel

from app.services.tokenize import tokenizer
from app.services.analyze import analyzer

app=FastAPI()

@app.get("/")
def info():
    return {
        "message": "Welcome",
        "for documentation":"go to /docs"
    }

@app.post("/tokenize")
def tokenize(text:str):
    return tokenizer(text)

@app.post("/analyze")
def analyze(text:str):
    return analyzer(text)