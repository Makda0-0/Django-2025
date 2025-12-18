import json

user_dict={
    "username":"Luna",
    "email":"luna@example.com",
    "active":True
}
json_string = json.dumps(user_dict,indent=4)
print("json_string: ")
print(json_string)