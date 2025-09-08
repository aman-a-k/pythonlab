from dataclasses import dataclass
@dataclass

class Student:
    name: str
    age: int 
    marks: int = 0 #Default value allowed 

s2 = Student("Anita", 21 , 85)
print(s2)
print(s2.name)
s2.age = 22                              #Can modify (mutable)
print(s2)                  