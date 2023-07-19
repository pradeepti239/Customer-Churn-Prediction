from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel):
    name: str
    salary: int = 50000

@app.get("/home")
def home():
    print("This is Home")
    return {"response":"200","msg":"Response received"}

@app.get("/about")
def about():
    print("This is About")
    return {"response":"200","msg":"Get Response received"}

@app.post("/insert")
def insert(data:Employee):
    print(data.name)
    print(data.salary)
    return {"response":"200","msg":"Post Response received"}



if __name__=="__main__":
    uvicorn.run("app:app", host = "localhost", port=8081, reload = True)


