from pydantic import BaseModel 

class User(BaseModel):
    id: int
    name: str
    email: str

users = {'id':'4', 'name':"John Doe", 'email':"new@gmail.com"}
student = User(**users)
# print(student.id, student.name, student.email)

print(student)
# print(type(student))