"""
def person(name, **data):
    print(name)

    for i, j in data.items():
        print(i, j)

person("Joyjeet", age = 21, city = "Asansol", mob = 12345667898)

"""

def person(name, *data):
    print(name)
    print(data)

person("Joyjeet", 21, "Asansol", 25374982374)