name_dictionary = {
    "Kenneth Angeles": "06/26/2005",
    "Camille Angeles": "10/20/2006",
    "Therese Angeles": "12/03/2010"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")

for item in name_dictionary.keys():
    print(item)
    
try:
    choose_bday = input("Who's birthday do you want to look up? ")
    name = name_dictionary[choose_bday]
    print("{}' birthday is {}.".format(choose_bday, name_dictionary[choose_bday]))
except KeyError:
    print("This person's name is not available to access.")
finally:
    print("Please choose a valid name from the list.")