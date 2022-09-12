# 5-1 Condition Tests

fruit = ['apple', 'pineapple', 'grapes', 'strawberry', 'oranges']
print('Is fruit[0] == apple I predict true')
print(fruit[0] == 'apple')

print("\nIs fruit[0] == pineapple I predict false")
print(fruit[0] == 'pineapple')

print("\nIs fruit[1] == pineapple I predict true")
print(fruit[1] == 'pineapple')

print("\nIs fruit[1] == grapes I predict false")
print(fruit[1] == 'grapes')

print("\nIs fruit[2] == grapes I predict true")
print(fruit[2] == 'grapes')

print("\nIs fruit[2] a strawberry I predict false")
print(fruit[2] == 'strawberry')

print("\nIs fruit[3] == strawberry I predict true")
print(fruit[3] == 'strawberry')

print("\nIs fruit[3] == oranges I predict false")
print(fruit[3] == 'oranges')

print("\nIs fruit[4] == oranges I predict true")
print(fruit[4] == 'oranges')

print("\nIs fruit[4] == apple I predict false")
print(fruit[4] == 'apple')


# 5.2 More condition tests
string = 'word'
print("\nIs string == word I predict true")
print(string == 'word')

print("\nIs string == Word I predict false")
print(string == 'Word')

# Test using lower() method
string = 'Word'
print("\nIs string.lower() == Word I predict false")
print(string.lower() == 'Word')

print("\nIs string.lower() == word I predict true")
print(string.lower() == 'word')

# Equality with Greater/less than with numbers
num1 = 10
print('\nIs 10 > 13 I predict false')
print(num1 > 13)

print('\nIs 10 < 13 I predict true')
print(num1 < 13)

# Tests using 'and' as well as 'or'
num2 = 5
print('\nIs 10 or 5 greater 8 I predict true')
print(num1 > 8 or num2 > 8)

print('\nIs 10 and 5 greater 8 I predict false')
print(num1 > 8 and num2 > 8)


list = ['Bible', 'President', 'Table', 'Clothes', 'Uniform']
# Checking if a word is in a list
if 'Bible' in list:
    print('\nThe word has been found!')

# Check if a word is not in the list
if 'Sociology' not in list:
    print('Sociology is not in the list')

    
# 5-3 Alien_Color
alien_color = 'yellow'
if alien_color == 'green':
    print('You have earned 5 points!')
if alien_color == 'red':
    print('You have earned 10 points!')

    
# 5-4 Alien_Colors #2
if alien_color == 'green':
    print('You have earned 5 points')
elif alien_color != 'green':
    print('You have earned 10 points')
else:
    print('Your color stinks')

    
# 5-5 Alien_Colors #3
if alien_color == 'green':
    print('You have earned 5 points')
elif alien_color == 'red':
    print('You have earned 10 points')
elif alien_color == 'yellow':
    print('You have earned 15 points')

    
#5-6 Stages of Life
age = 18
if age < 2:
    print('Baby')
elif age < 4:
    print('toddler')
elif age < 13:
    print('Kid')
elif age < 20:
    print('Teenager')
elif age < 65:
    print('Adult')
else:
    print('Elderly')

    
# 5-7 Favorite fruits
fruit_list = ['apple', 'kiwi', 'pear']
if 'apple' in fruit_list:
    print("Wow you really like apples!")
if 'kiwi' in fruit_list:
    print("Wow you really like kiwi")
if 'pineapple' in fruit_list:
    print("Wow you really like pineapple")
if 'strawberry' in fruit_list:
    print("Wow you really like strawberry")
if 'pear' in fruit_list:
    print("Wow you really like pear")

# 5-8 Hello Admin

usernames = ['patty']
for names in usernames:
    if names == 'admin':
        print("Hello admin, would you like to see the status report?")
    elif names != 'admin':
        print(f"Hello {names.title()}, thank you for logging in today!")
#5-9 No Users
if len(usernames) == 0:
    print('We need to find some users!')

# 5-10 Checking Usernames
current_users = ['twisted_weasel', 'boxing_flea', 'concrete_street', 'doodle', 'awful_cobra']
new_users = ['doodle', 'apple', 'jacky_chan', 'twisted_weasel', 'grechy']
for titles in current_users:
    titles.upper()
for title in new_users:
    title.upper()
for names in new_users:
    if names in current_users:
        print(f'Sorry {names} is taken')
    else:
         print(f'{names} works great!')

print("\n")
# 5-11 Ordinal Numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num == 1:
        print("1st")
    elif num == 2:
        print('2nd')
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")
