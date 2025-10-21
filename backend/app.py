import os
from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
