from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get("/")
def info():
    return {
        "message": "Welcome",
        "for documentation":"go to /docs"
    }