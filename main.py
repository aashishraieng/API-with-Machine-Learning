from fastapi import  FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/square/{number}")
def square_number(number:int):
    result=number**2
    return {"number":number,"square":result}


@app.get("/add")
def add_number(a:int,b:int):
    result=a+b
    return {"a":a,"b":b,"result":result}



# class Person(BaseModel):
#     name:str
#     age:int
#     slary:float

# @app.post("/person")
# def create_person(person:Person):
#     if person.age < 0:
#         return {"error":"Age cannot be negative"}
    
#     return {"name":person.name,"age":person.age,"salary":person.slary}


with open("salary_model.pkl", "rb") as f:
    model = pickle.load(f)

class Person(BaseModel):
    age: int
    salary: float
@app.post("/predict")
def predict(person: Person):

    data = [[person.age, person.salary]]

    prediction = model.predict(data)

    return {
        "age": person.age,
        "salary": person.salary,
        "prediction": prediction[0]
    }