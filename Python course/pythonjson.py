import json

person= '{"name":"Bob", "labguages":["English","French"]}'
person_dict = json.loads(person)

print(person_dict)
print(person_dict['languages'])

#open a json file

with open("data.json") as f:
    data = json.load(f)

print(data)    