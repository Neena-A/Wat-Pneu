from fastapi import FastAPI 
import finalnet as fn

app=FastAPI()

@app.get("/")
def home():
    print("API working")

@app.get("/start")
def work():
    fn.main_call()