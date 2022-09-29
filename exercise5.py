# 8.1 Message
def display_message():
    print("This chapter will teach you all about functions and how to use them!")

display_message()

print("\n")

# 8.2 Favorite Book
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}")

favorite_book("Alice in wonderland")

print("\n")

# 8.3 T-Shirt and 8.4 Large Shirts
def make_shirt(message = 'I love Python', size='Large'):
    print(f"You have ordered a {size} shirt that says {message} on it!")

make_shirt("You're a winner", "large")
make_shirt()
make_shirt(size='Medium')
make_shirt(message='You are so cool')

print('\n')

# 8.5 Cities
def describe_city(city="Greenville", country="United States"):
    print(f"{city} is in {country}")

describe_city()
describe_city('Paris', 'France')
describe_city('Berlin', 'Germany')
describe_city('New York')

print("\n")

# 8.6 City Names
def city_country(city="", country=""):
    print(f"{city}, {country}")

city_country("Santiago", "Chile")
city_country("Berlin", "Germany")
city_country("Greenville", "United States")

print("\n")

# 8.7 Albums and 8.8 User Albums
def make_album(artist, album, song=None):
    if song:
        cover = {'Artist': artist, 'Album': album, "Total Songs": song}
    else:
        cover = {"Artist": artist, 'Album': album}
    return cover
print(make_album("Zach Bryan", "American Heartbreak"))
print(make_album("Juice WRLD", "Goodbye & Good Riddance"))
print(make_album("Post Malone", "Hollywood's Bleeding"))
print(make_album("Kid Cudi", "Man on the Moon III", 17))
answer3 = "stop"
print("If you want to stop, type in 'stop' at the end")
while answer3 != 'stop':
    singer = "What is an artist?"
    album_name = "What is one of his albums?"
    answer1 = input(singer)
    answer2 = input(album_name)
    print(make_album(answer1, answer2))
    answer3 = input("Would you like to stop?")

print("\n")

# 8.9 Messages
list = ["You got it", "I believe in you", "Coding is so cool!", "I am proud to be a cyber kid"]
def show_messages(messages):
    for message in messages:
        print(message)
show_messages(list)

print("\n")

# 8.10 Sending Messages and 8.11 Archived Message
sent_messages = []
list = ["You got it", "I believe in you", "Coding is so cool!", "I am proud to be a cyber kid"]
def send_messages(messages):
    for message in messages:
        print(message)
        sent_messages.append(list.pop())

show_messages(list[:])
print(list)

print("\n")
# 8.12 Sandwiches
def sandwich(*toppings):
    print(f"Your sandwich has these toppings on it: ")
    for topping in toppings:
        print(topping)
sandwich("turkey", 'lettuce', 'honey mustard')
sandwich("ham", "salami", "lettuce", "tomato")
sandwich("meatballs", "mozzarella")

print("\n")

# 8.13 User Profiles
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
my_profile = build_profile("Patrick", "Bratten", haircolor='blonde', height="5'8", heritage="Irish")
print(my_profile)

print("\n")

# 8.14 Cars
def make_car(manufacture, model, **stuff):
    print(manufacture)
    print(model)
    print(stuff)
car = make_car('Honda', "Civic", color = 'blue', shape = 'round')

print("\n")

# 8.15 Printing Models
#I could not find the example of printing_models.py to copy so I made a function myself
from printing_models import print_words
print_words("Hopefully this still works. I only saw examples for pizza functions.")

print("\n")

# 8.16 Imports
import functions_practice
from functions_practice import car_info
from functions_practice import car_info as ci
import functions_practice as fp
from functions_practice import *
functions_practice.car_info("Honda", "Civic")
car_info("Toyota", "Corrola")
ci("Chevy", "Trail Blazer")
fp.car_info("Kia", "Optima")

#8.17 Styling Functions
#All good here Chief!
