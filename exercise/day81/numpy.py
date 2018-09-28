import json


x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)


print(y["age"])
