import json
json_string = '''
{
    "products":"laptop",
    "price":75000,
    "available":true 
}  
'''
data = json.loads(json_string)


print("product:", data["products"]) 
print("price:", data["price"])   