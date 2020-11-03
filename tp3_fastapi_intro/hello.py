from fastapi import FastAPI

myApp = FastAPI()

@myApp.get("/")
def hello():
    return ("Hello Word")