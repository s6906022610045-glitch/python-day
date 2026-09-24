import json

date = {"name": "Alice", "age": 25}
json_str = json.dumps(date)
print(json_str)

parsed_date = json.loads(json_str)
print(parsed_date)
print(parsed_date["name"])
print(parsed_date["age"])