import json

filename = 'test.json'

with open(filename) as f:
    json_data = json.load(f)
    print(json_data)