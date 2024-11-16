person1 = {
    "name": "Pablo",
    "age": 24,
    "working": True
}

person2 = dict(
    name = "Kevin", 
    age = 23, 
    working = False
)

people = [person1, person2]

for person in people:
    print(f"Me llamo {person["name"]} tengo {person["age"]} años y{" no" if not person["working"] else ""} estoy trabajando")
    
