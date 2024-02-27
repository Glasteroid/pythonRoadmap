import datetime

name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

now = datetime.datetime.now()

age_100 = 100 - age + now.year

print(f"{name}, you will turn 100 in year {age_100}.")