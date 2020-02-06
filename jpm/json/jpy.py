import json

people_str = '''
{
    "firstName": "Rack",
    "lastName": "Jackon",
    "gender": "man",
    "age": 24,
    "address": {
        "streetAddress": "126",
        "city": "San Jone",
        "state": "CA",
        "postalCode": "394221"
    },
    "phoneNumbers": [
        { "type": "home", "number": "7383627627" }
    ]
}
'''

print people_str
print (type(people_str))
data = json.loads(people_str)
print data
print (type(data))

new_str = data["phoneNumbers"]
newj = json.dumps(data, indent=2, sort_keys = True)
print newj
print (type(newj))

with open ('test.json') as f:
    d=json.load(f)

print "newly opended from file %s" %d

with open ('new_json.json', 'w') as f:
    json.dump(d, f, indent=2)

