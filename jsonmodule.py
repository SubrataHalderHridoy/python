import json

d={
    "name": "hridoy",
    "age": 21,
    "isTeacher": True
}

with open("data.json", "w") as f:
    json.dump(d, f, indent=4, sort_keys=True)
    






