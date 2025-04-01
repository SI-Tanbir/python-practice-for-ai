import json


# data=[
#   {
#     "name": "John Doe",
#     "age": 28,
#     "sex": "Male",
#     "occupation": "Software Engineer"
#   },
#   {
#     "name": "Jane Smith",
#     "age": 34,
#     "sex": "Female",
#     "occupation": "Doctor"
#   }
 
# ]

# #sterilazation data: json --> python
# json_data=json.dumps(data)

# print(json_data)


# #sterilazation data: python --> json
pythondata = '''[
    {
        "name": "John Doe",
        "age": 28,
        "sex": "Male",
        "occupation": "Software Engineer"
    }
]'''

# sterilazation data: json --> python
python_data=json.loads(pythondata)  
print(type(python_data))






