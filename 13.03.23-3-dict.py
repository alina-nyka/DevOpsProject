# importing the module
# ast package evaluate a string to an Object of python,
# returning a dictionary
import ast

# reading the data from the file
with open('dict.txt') as f:
    data = f.read()
    d = ast.literal_eval(data)

print(d["name"])
print(f"name: {d['name']}, age = {d['age']}")
