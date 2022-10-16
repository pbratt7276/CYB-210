from random import *

upper_points = 0
lower_points = 0
ones = True
twos = True
threes = True
fours = True
fives = True
sixes = True
toak = True
foak = True
fullhouse = True
smstraight = True
lgstraight = True
yahtzee = True
chance = True
categories_boolean = [ones, twos, threes, fours, fives, sixes, toak, foak, fullhouse, smstraight,
                      lgstraight, yahtzee, chance]
categories_names = ['Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Toak', 'Foak', 'Fullhouse', 'Smstraight',
                    'Lgstraight', 'Yahtzee', 'Chance']


class Dice:
    """Initialize the values of the dice, Roll and Re-Roll the Dice, Check if the dice match the category chosen
    and allocate the points necessary"""

    def __init__(self):
        """Initializes each die and creates the attribute turn as well as add the dice to a list"""
        self.die1 = 0
        self.die2 = 0
        self.die3 = 0
        self.die4 = 0
        self.die5 = 0
        self.dice = [self.die1, self.die2, self.die3, self.die4, self.die5]
        self.turn = 0

    def roll_dice(self):
        """Give each dice a random number 1-6 and add to the turn counter"""
        self.die1 = randint(1, 6)
        self.die2 = randint(1, 6)
        self.die3 = randint(1, 6)
        self.die4 = randint(1, 6)
        self.die5 = randint(1, 6)
        self.dice = [self.die1, self.die2, self.die3, self.die4, self.die5]

    def reroll_dice(self, my_list=None):
        """Re-rolls the dice chosen by the user and adds 1 to the turn counter"""
        pass

        if my_list is None:
            my_list = []
        for num in my_list:
            if num == '1':
                self.die1 = randint(1, 6)
            elif num == '2':
                self.die2 = randint(1, 6)
            elif num == '3':
                self.die3 = randint(1, 6)
            elif num == '4':
                self.die4 = randint(1, 6)
            elif num == '5':
                self.die5 = randint(1, 6)
        self.dice = [self.die1, self.die2, self.die3, self.die4, self.die5]
        self.turn += 1

    def checker(self, category_input):
        """Check if the user's dice roll matches the category selected and then allocate the points if necessary"""
        global ones
        global twos
        global threes
        global fours
        global fives
        global sixes
        global toak
        global foak
        global fullhouse
        global smstraight
        global lgstraight
        global yahtzee
        global chance
        global lower_points
        global upper_points

        if category_input == 'ones':
            for i in self.dice:
                if i == 1:
                    upper_points += 1
            ones = False

        elif category_input == 'twos':
            for i in self.dice:
                if i == 2:
                    upper_points += 2
            twos = False

        elif category_input == 'threes':
            for i in self.dice:
                if i == 3:
                    upper_points += 3
            threes = False

        elif category_input == 'fours':
            for i in self.dice:
                if i == 4:
                    upper_points += 4
            fours = False

        elif category_input == 'fives':
            for i in self.dice:
                if i == 5:
                    upper_points += 5
            fives = False

        elif category_input == 'sixes':
            for i in self.dice:
                if i == 6:
                    upper_points += 6
            sixes = False

        elif category_input == 'toak':
            sort_category = self.dice
            sort_category.sort()
            if sort_category[0] == sort_category[2] or sort_category[1] == sort_category[3] \
                    or sort_category[2] == sort_category[4]:
                for i in self.dice:
                    lower_points += i
            toak = False

        elif category_input == 'foak':
            sort_category = self.dice
            sort_category.sort()
            if sort_category[0] == sort_category[3] or sort_category[1] == sort_category[4]:
                for i in self.dice:
                    lower_points += i
            foak = False

        elif category_input == 'fullhouse':
            sort_category = self.dice
            sort_category.sort()
            if sort_category[0] == sort_category[2] and sort_category[3] == sort_category[3]:
                lower_points += 25
            elif sort_category[0] == sort_category[1] and sort_category[2] == sort_category[4]:
                lower_points += 25
            fullhouse = False

        elif category_input == 'smstraight':
            sort_category = self.dice
            sort_category.sort()
            if sort_category[0] < sort_category[1] < sort_category[2] < sort_category[3]:
                lower_points += 30
            elif sort_category[1] < sort_category[2] < sort_category[3] < sort_category[4]:
                lower_points += 30
            smstraight = False

        elif category_input == 'lgstraight':
            sort_category = self.dice
            sort_category.sort()
            if sort_category[0] < sort_category[1] < sort_category[2] < sort_category[3] < sort_category[4]:
                lower_points += 40
            lgstraight = False

        elif category_input == 'yahtzee':
            if self.die1 == self.die2 == self.die3 == self.die4 == self.die5:
                lower_points += 50
            yahtzee = False

        elif category_input == 'chance':
            for i in self.dice:
                lower_points += i
            chance = False


# Introduction and small explanation of the rules
print("Welcome to Patty's Yahtzee!")
print("\nBefore we get started, You should know that some of the category names have been abbreviated: \nThree-of-a-"
      "kind is Toak, Four-of-a-kind is Foak, Small Straight is Smstraight, and Large Straight is Lgstraight."
      "\nWhen you are asked to enter which category you would like to apply the dice to, you must enter the exact"
      " abbreviation or name listed in the categories.\nAlso, when you are asked which dice to re-roll"
      "Don't use the number that you rolled on the dice. You should use which die it was.\n"
      "For example, if you rolled 2 4 3 5 3, die 1 correlates to the number 2, die 2 correlates "
      "to number 4, and so on. \nSo if you were to re-roll those two dice, you would type 1,2 \nGood Luck!\n")

# Creating the object used for the program
me = Dice()

# While loop that ends once every category has been used
while ones or twos or threes or fours or fives or sixes or toak or foak or fullhouse or smstraight or lgstraight or \
        yahtzee or chance == True:
    # Prints the remaining categories the user needs to do
    print("Here are the remaining categories you need: ")
    for i in categories_names:
        print(f"  -{i}")

    # Rolls the first dice for the user
    print("\nLet this round begin! Here is the first roll: \n")
    me.roll_dice()
    print(me.die1, me.die2, me.die3, me.die4, me.die5)
    me.turn = 0
    while me.turn < 2:
        roll_again = input("\nWould you like to roll the dice? y for YES or n for NO ")

        # If the user wishes re-roll some dice
        if roll_again.lower() == 'y':
            digits = input("Which dice would you like to re-roll (format ex: 1,3,4): ")
            digits = digits.split(",")
            me.reroll_dice(digits)
            print(me.die1, me.die2, me.die3, me.die4, me.die5)

        # If the user chooses not to roll their remaining attempts
        elif roll_again == 'n':
            category = input("What category would you like to apply the dice roll to? ")
            me.checker(category.lower())
            categories_names.remove(category.title())
            print(f"\nFor the upper section, you now have {upper_points} points")
            print(f"\nFor the lower section, you now have {lower_points} points\n")
            break

        # In case the user does not type 'y' or 'n' when asked if they want to roll the dice
        else:
            print("You must enter 'y' or 'n' when asked if you would like to roll the dice")

        # If the user has re-rolled their two attempts
        if me.turn == 2:
            category = input("What category would you like to apply the dice roll to? ")
            me.checker(category.lower())
            categories_names.remove(category.title())
            print(f"\nFor the upper section, you now have {upper_points} points")
            print(f"\nFor the lower section, you now have {lower_points} points\n")

# Allocates the bonus points for Upper Section if they had enough points
if upper_points > 62:
    upper_points += 35
    print("Congratulations! You have now received the bonus for the Upper Section for having 63 or more points!"
          "35 Points have now been added to your Upper Section Score!")

print(f"Your final score for the Upper Section was {upper_points} points\n"
      f"Your final score for the Lower Section was {lower_points} points\n"
      f"Your final score was {upper_points + lower_points}!!!"
      f"\nThank you for playing and Please come play again at any time!")

# All of this code was written by me and not stolen or borrowed from any previous works
