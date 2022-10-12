# 9.1 Restaurants, 9.2 Three Restaurants, 9.4 Number Served

from typing import *
from restaurant_import import *
from users_import import *


my_restaurant = restaurant('JPeters', "American")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# 9.4 Specific Prints
print(my_restaurant.number_served)
my_restaurant.set_numbers_served(24)
my_restaurant.describe_restaurant()
my_restaurant.increment_numbers_served(32)
my_restaurant.describe_restaurant()


print("\n")

# 9.3 Users and 9.5 Login Attempts
"""These classes and methods can be found in the users_import"""

Me = users('Will', 'Bratten', 19, 'Male')
Me.describe_user()
Me.greet_user()
Me.increment_login_attempts()
Me.increment_login_attempts()
print(Me.login_attempts)
Me.reset_login_attempts()
print(Me.login_attempts)
You = users('Brandon', 'Grech', 30, 'Male')
You.describe_user()
You.greet_user()

print("\n")

# 9.6 Ice Cream Stand

class IceCreamStand(restaurant):
    """Inherits the Restaurant class and adds the flavours they have available"""
    def __init__(self, name, cuisine):
        """Initialize the attributes of name and cuisine"""
        super().__init__(name, cuisine)
        self.flavours = ['Chocolate', 'Vanilla', 'Strawberry', 'Birthday Cake']
    def show_flavours(self):
        """Print out the flavours"""
        print(self.flavours)

the_restaurant = IceCreamStand("Longhorn Steak House", "American")
print(f"{the_restaurant.flavours} are the flavours offered")
the_restaurant.show_flavours()

print("\n")

# 9.7 Admin and 9.8 Privileges
"""These classes and methods are in the users_import file"""

boss = Privileges("Skylar", "Bruner", 19, "Female")
boss.show_privileges()

print("\n")

# 9.9 Battery Upgrade
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100
car = Battery()
print(f"{car.battery_size}% battery life")
car.upgrade_battery()
print(f"{car.battery_size}% battery life")

print("\n")

# 9.10 Imported Restaurant
"""Put the Restaurant class without the inherited classes into restaurant_import.py"""
"""Imported Restaurant at the top"""
Maki = restaurant('Maki', 'Japanese')
Maki.describe_restaurant()

print("\n")

# 9.11 Imported Admin
"""Use the User methods and child classes from the import"""
Avery = Privileges("Avery", "Walters", 18, "Female")
Avery.show_privileges()

print("\n")

# 9.12 Multiple Modules

# 9.13 Dice
from random import *
class Die:
    """Rolls the dice"""

    def __init__(self, sides):
        self.sides = int(sides)

    def roll_die(self):
        """Roll die and show die"""
        print(randint(1, self.sides))

dice = Die(6)
die = Die(10)
dices = Die(20)

dice.roll_die()
die.roll_die()
dices.roll_die()

print("\n")

# 9.14 Lottery and 9.15 Lottery Analysis

def check():
    my_ticket = "abcd"
    count = 0
    winning_num = ''
    while my_ticket != winning_num:
        list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd']
        first_choice = str(choice(list))
        second_choice = str(choice(list))
        third_choice = str(choice(list))
        fourth_choice = str(choice(list))
        winning_num = first_choice + second_choice + third_choice + fourth_choice
        count += 1
    return count

#9.15 Lottery Analysis
print(f"It took {check()} times for your number to match the winner!")

print("\n")

# 9.16 isn't at a problem, so I assume this doesn't count as skipping one.

# 10.1 Learning Python

with open('learning_python.txt') as file_object:
    contents = file_object.read()
print(contents)

print("\n")

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line)

print("\n")

list = []
with open('learning_python.txt') as file_object:
    for line in file_object:
        list.append(line)
print(list)

print('\n')

# 10.2 Learning C skipped
# 10.3 Guest and 10.4 Programming Poll
Input = ''
while Input != 'stop':
    Input = input("What is your name?")
    if(Input != 'stop'):
        with open('guest.txt', 'a') as file_object:
            file_object.write(f"{Input} \n")
            print(f"Glad you could make it {Input}!")

with open('guest.txt') as file_object:
    message = file_object.read()
    print(message)

print("\n")

# 10.5 Programming Poll
reason = ''
while reason != 'stop':
    reason = input("What are your thoughts on programming")
    if reason != 'stop':
        with open('programming_poll.txt', 'a') as file_object:
            file_object.write(f"{reason} \n")

print("\n")

# 10.6 Addition and 10.7 Addition Calculator
number1 = ''
number2 = ''
while number1 != 'q' or number2 != 'q':
    number1 = input("Pick a number")
    number2 = input("Pick another number")
    if number1 or number2 != 'q':
        try:
            sum_number = int(number1) + int(number2)
        except ValueError:
            print("You must input a number")
        else:
            print(sum_number)

print("\n")

# 10.8 and 10.9
try:
    with open('cat.txt') as cat_txt:
        print(cat_txt.read())
    with open('dog.txt') as dog_txt:
        print(dog_txt.read())
except FileNotFoundError:
    print("This file was not found")


