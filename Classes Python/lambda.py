people = [
    {"name": "Harry","house": "gryffindor"},
    {"name": "Cho","house": "ravenclaw"},
    {"name": "Draco","house": "slytherin"},   
]

people.sort(key=lambda person: person["name"])

print(people)