# Nested dictionary
student = {
    "name": "Ushashi",
    "age": 20,
    "address": {
        "street": "123 Main St",
        "city": "New York City",
        "state": "New York",
        "Country": "USA"
    }
}
print(student)
print(student["address"])
print(student["address"]["city"])
print(len(student))
print(len(student["address"]))
       