import json

with open('info.json', 'r') as f:
    info = json.load(f)
    
print("Welcome to the birthday dictionary. We know the birthdays of:")

for item in info.keys():
    print(item)
    
try:
    choose_bday = input("Who's birthday do you want to look up? ")
    name = info[choose_bday]
    print("{}' birthday is {}.".format(choose_bday, info[choose_bday]))
except KeyError:
    print("Please choose a valid name from the list.")