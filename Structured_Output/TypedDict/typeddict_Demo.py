from typing import TypedDict

class car(TypedDict):
    model:str
    price:int

car1:car = {
    "model":"BMW",
    "price":100000
}

car2:car = {
    "model":"BMW",
    "price":"100000"
}

print(car1)
print(car2)