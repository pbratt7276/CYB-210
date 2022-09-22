
# Problem 1 Create a dictionary and print the values
myself = {
    'f_name': 'Patrick',
    'l_name': 'Bratten',
    'hometown': 'Fountain Inn',
    'current_city': 'Anderson',
    'username': 'pbratt7276'
}
print(myself)
for key, value in myself.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Problem 2 Printing keys and values with more information
for key, value in myself.items():
    if key == 'f_name':
        print(f"First name is {value}")
    elif key == 'l_name':
        print(f"Last name is {value}")
    elif key == 'username':
        print(f"Username is {value}")
    elif key == 'hometown':
        print(f"For privacy reasons, their hometown is {myself['hometown']}")

# Problem 3-4 Dictionary with definitions
dictionary = {
    'Python': 'A programming language',
    'Variable': 'A word you can store information in',
    'List': 'Stores multiple words or variables',
    'Method': 'Executes an action on a variable or object',
    'If statement': 'Checks if something is true or false',
    'Dictionary': 'Stores keys and values',
    'Function': 'Executes actions on something'
}
print("\n\n")
for key, value in dictionary.items():
    print(f"{key}: {value}")

# Problem 5 Create a dictionary with 6 counties

counties = {
    'Anderson County': 'Anderson',
    'Greenville County': 'Greenville',
    'Greenwood County': 'Greenwood',
    'Charleston County': 'Charleston',
    'Aiken County': 'Aiken',
    'Spartunburg County': 'Spartunburg'
}
# Problem 6 Checking if counties are in the Dictionary
counties_list = ['Greenville County', 'Anderson County', 'Greenwood County', 'Charleston County', 'Aiken County',
                 'Spartunburg County', 'Kershaw County', 'Laurens County', 'Orangeburg County', 'Pickens County']
print('\n\n')
for key in counties_list:
    if key in counties:
        print(f"{key} is in our dictionary, and the capital seat is {counties[key]}")
    elif key not in counties:
        print(f"{key} is not in our dictionary. We will add this county shortly. Thanks!")


# Problem 7 Nested dictionary inside of a List
greenville_county = {
    'Greenville': 69648,
    'Taylors': 23107,
    'Simpsonville': 23200,
    'Mauldin': 25829,
    'Wade Hampton': 20192
}
charleston_county = {
    'Mount Pleasant': 89410,
    "Sullivan's Island": 2177,
    'Edisto Island': 2301,
    'Isle of Palms': 4371,
    'Folly Beach': 2664,
}
beaufort_county = {
    'Beaufort': 13417,
    'Hilton Head Island': 40000,
    'Parris Island': 4841,
    'Shell Point': 2991,
    'Port Royal': 13265
}
horry_county = {
    'Conway': 24747,
    'Myrtle Beach': 33638,
    'Garden City': 11193,
    'North Myrtle': 16684,
    'Surfside Beach': 4470,
}
union_county = {
    'York': 8297,
    'Rock Hill': 74410,
    'Fort Mill': 19920,
    'Clover': 6370,
    'Newport': 4432
}
print('\n\n')
counties_cities_list = [greenville_county, charleston_county, beaufort_county, horry_county, union_county]
for county in counties_cities_list:
    for key, value in county.items():
        print(f"In {key}, the current population is {value} ")


#  Problem 8: Lists nested in Dictionaries
sc_counties = {
    'Greenville County': ['Greenville', 'Simpsonville', 'Mauldin'],
    'Charleston County': ['Mount Pleasant', 'Isle of Palms', 'Folly Beach'],
    'Horry County': ['Garden City', 'North Myrtle Beach', ' Surfside Beach']
}
for key, value in sc_counties.items():
    print(f"In {key}, the largest cities are: ")
    for county in value:
        print(f"\t {county}")
print("\n\n")
# User Input Problem 1
message = input("What is your first and last name?: ")
print(f"Welcome to Anderson, {message}!")

print("\n\n")

# User Input Problem 2 Money Budget

money = int(input("How much money do you have?: "))
if money < 50:
    print("Your best option is the i3 processor")
elif money < 100:
    print("You should buy an i5 processor")
elif money <150:
    print("i7 processor is the way to go")
else:
    print("I personally would recommend the i9 processor")


# User Input Problem 3 & 4 Odd vs Even/ requirements
print("Its time to test what numbers are even or odd! If you want to stop, type stop.")
integer = ''
while integer != 'stop':
    integer = input("Pick any integer: ")
    if integer.lower() == 'stop':
        break
    elif int(integer) % 2 == 0:
        print(f"{int(integer)} is an even number!")
    elif int(integer) % 2 == 1:
        print(f"{int(integer)} is an odd!")

# User Input Problem 5 Ubuntu Flavours
total = 0
while total <= 50:
    poll = {'name': [], 'flavour': []}
    username = input("What is your username?: ")
    poll['name'].append(f"{username}")
    opinion = input("What is your favorite Unbuntu Flavour?")
    if opinion.lower() == 'kubuntu' or opinion.lower() == 'lubuntu' or opinion.lower() == 'ubuntu budgie' or opinion.lower() == 'unbuntu kylin' or opinion.lower() == 'unbuntu studio' or opinion.lower() == 'unbuntu mate' or opinion.lower() == 'xubuntu':
        poll['flavour'].append(f"opinion")
        print("Thank you so much for taking the survey!")
        total += 1
    else:
        print("Please try again. That was not an acceptable option")
