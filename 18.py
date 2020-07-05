# json to inspect the attributes of the module

import json

# dump - serialize object

data_serialize = {
    "name": "Mel Gibson",
    "hobbies": ['travelling', 'reading', 'hiking'],
    "address": ('Nepal', 'Lalitpur'),
    "age": 29
}

jsserial = json.dumps(data_serialize)
print(jsserial)

# loads - deserialize to a python object


data_deserialize = '{"name": "Mel Gibson", "age": 29 }'

parsed = json.loads(data_deserialize)
print(parsed)

print(parsed["name"])
