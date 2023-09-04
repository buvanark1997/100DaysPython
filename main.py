# tip calculation program
import random
import camelcase
from replit import clear
def calculateTip():
    print("Welcome to the tip calculator")
    totalBill = float(input("What was the total bill?"))
    tipPercentage = int(input("What percentage tip would you like to give ?"))
    people = int(input("How many people to split the bill?"))

    tipValue = round(totalBill, 2) * (tipPercentage / 100)
    share = (tipValue + totalBill) / people
    formatted_Share = "{:.2f}".format(share)  # it will print the last value even if its "0"
    print(f"Each person should pay: {round(share, 2)}")  # if last digit is "0" round will not print 0
    print(f"Each person should pay: {formatted_Share}")


def order_Pizza():
    print("Welcome to python pizza deliveries !")
    size = str(input("Enter pizza size. S, M or L?"))
    addOn = str(input("Do you need papproni on top? Y or N"))
    exCheese = str(input("Do you need extra cheese on top? Y or N"))
    price = 0
    if size.lower() == 's':
        price += 15
        if addOn.lower() == 'y':
            price += 2
    elif size.lower() == 'm':
        price += 20
        if addOn.lower() == 'y':
            price += 3

    elif size.lower() == 'l':
        price += 25
        if addOn.lower() == 'y':
            price += 3

    if exCheese.lower() == 'y':
        price += 1

    print(f"Your final bill is: ${price}")


def loveCalculator():
    first_digit_letters = ["t", "r", "u", "e"]
    second_digit_letters = ["l", "o", "v", "e"]
    name1 = str(input("What is your name?\n"))
    name2 = str(input("What is their name?\n"))
    name = name2 + name1
    first_digit = 0
    second_degit = 0
    for fl in first_digit_letters:
        first_digit += name.count(fl)
    for fl in second_digit_letters:
        second_degit += name.count(fl)
    finalValue = str(first_digit) + str(second_degit)
    Message = ""
    if int(finalValue) < 10 or int(finalValue) > 90:
        Message = f"Your score is {finalValue}, you go together like coke and mentos"
    elif int(finalValue) >= 40 and int(finalValue) <= 50:
        Message = f"Your score is {finalValue}, you are alright together"
    else:
        Message = f"Your score is {finalValue}"

    print(Message)


# get random number from the computer which is not decided from us

def random_exercise():
    print(random.randint(1, 10000))
    print(random.random())


# program to pick random value from the list
def payBills():
    inputStr = input("Enter list of names \n")
    listNames = inputStr.split(",")
    length = len(listNames)
    randomValue = random.randint(0, length - 1)
    print(f"{listNames[randomValue]} is going to pay for the meal")


def combiningList():
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]
    list_combined = [list1, list2]
    print(list_combined[0][0])


def TreasureMap():
    row1 = ["😏", "😏", "😏"]
    row2 = ["😏", "😏", "😏"]
    row3 = ["😏", "😏", "😏"]
    row = [row1, row2, row3]
    indexValue = input(
        "Enter the index to mark")  # first digit represents column position second represents row position
    rowValue = int(indexValue[1]) - 1
    colValue = int(indexValue[0]) - 1
    row[rowValue][colValue] = "X"
    print(f"{row1}\n{row2}\n{row3}")


def rock_paper_scissors():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    your_choice = int(input("What do you choose? 0 for Rock,1 for Paper and 2 for Scissors."))
    print("Your choice")
    if your_choice == 0:
        print(rock)
    elif your_choice == 1:
        print(paper)
    else:
        print(scissors)
    choiceArray = ["rock", "paper", "scissors"]
    computerChoice = choiceArray[random.randrange(0, len(choiceArray) - 1)]
    print("Computer choice")
    if computerChoice == "rock":
        print(rock)
    elif computerChoice == "paper":
        print(paper)
    else:
        print(scissors)

    if your_choice == 0 and computerChoice.lower() == "scissors":
        print("You win")
    elif your_choice == 0 and computerChoice.lower() == "paper":
        print("You lose")
    elif your_choice == 2 and computerChoice.lower() == "rock":
        print("You lose")
    elif your_choice == 2 and computerChoice.lower() == "paper":
        print("You win")
    elif your_choice == 1 and computerChoice.lower() == "rock":
        print("You win")
    elif your_choice == 1 and computerChoice.lower() == "scissors":
        print("You lose")
    else:
        print("Draw")


# find the highest score from the list without using in-build functions

def highest_Score():
    scoreList_Str = input("Enter list of scores: ")
    scoreList = scoreList_Str.split(',')
    maxScore = 0
    for i in scoreList:
        if int(i) > maxScore:
            maxScore = int(i)

    print(maxScore)


# fizzbuzz game - print number from 1 to 100 for no divisible by 3 print fizz
# for no divisible by  5 print buzz
# and no div by 3,5 print fizzbuzz

def fizzbuzz():
    for no in range(1, 101):
        message = ""
        if no % 3 == 0:
            message = "Fizz"
        if no % 5 == 0:
            message += "Buzz"
        elif no % 3 != 0 and no % 5 != 0:
            message = str(no)
        print(message)


def password_Generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to the PyPassword Generator!")
    generated_password = ""
    randomized_password = ""
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    for i in range(0, nr_letters):
        randomValue = random.randint(0, len(letters) - 1)
        generated_password += letters[randomValue]
    for i in range(0, nr_symbols):
        randomValue = random.randint(0, len(symbols) - 1)
        generated_password += symbols[randomValue]
    for i in range(0, nr_numbers):
        randomValue = random.randint(0, len(numbers) - 1)
        generated_password += numbers[randomValue]
    generated_password = list(generated_password)
    generated_password = random.sample(generated_password, len(generated_password))
    generated_password = ''.join(generated_password)  # to convert list to string
    print(f"Here is your password: {generated_password}")


def Hangman_Exer1():
    words = ['Moon', 'ISRO', 'VikramLander']
    selectedWord = random.choice(words)
    ic = input("Enter letter")
    for c in selectedWord:
        if ic.lower() == c.lower():
            print("Right")
        else:
            print("Wrong")


def Hangman_Exer2():
    stages = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']
    words = ['Moon', 'ISRO', 'VikramLander']
    selectedWord = random.choice(words)
    print(selectedWord)
    blankWord = ""
    lives = 6
    for l in selectedWord:
        blankWord += "_"
    while lives > 0:
        ic = input("Enter letter")
        for i in range(0, len(selectedWord)):
            if ic.lower() == selectedWord[i].lower():
                blankWord = list(blankWord)
                blankWord[i] = ic
        print(''.join(blankWord))
        if ic not in selectedWord:
            lives = lives - 1
            end_of_game = True

            if lives == 0:
                print("You Lose")

    if '_' not in blankWord:
        print("You Won")
    print(stages[lives])


from caeserArt import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def CaeserCipher():
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    secretMessage = ""
    appendmsg = ""
    while shift > 52:
        shift = shift % len(alphabet)
    for t in text:
        if t.isalpha():
            index = alphabet.index(t)
            if direction == 'encode':
                index += shift
            else:
                index -= shift
            appendmsg = alphabet[index]
        else:
            appendmsg = t
        secretMessage += appendmsg

    print(f" your {direction}d message is {secretMessage}")


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62
}


# Dictionary
def findResult():
    Result_Student = {}
    for stu in student_scores:
        if student_scores[stu] >= 91:
            Result_Student[stu] = "Outstanding"
        elif 81 <= student_scores[stu] <= 90:
            Result_Student[stu] = "Exceeds Expectations"
        elif 71 <= student_scores[stu] <= 80:
            Result_Student[stu] = "Acceptable"
        else:
            Result_Student[stu] = "Fail"

    print(Result_Student)


# nesting dictinary in a dictionary
travel_log_dict = {
    "France": {"Cities_visited": ["Paris", "Lille", "Dijon"], "Total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}
# nesting dictionary in a list
travel_log_list = [
    {
        "Country": "France",
        "Cities_visited": ["Paris", "Lille", "Dijon"],
        "Total_visits": 12
    },
    {
        "Country": "Germany",
        "Cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Total_visits": 5
    }
]


def add_new_country(country, no_of_visits, citiesList):
    new_list = {
        "Country": country,
        "Cities_visited": citiesList,
        "Total_visits": no_of_visits
    }
    travel_log_list.append(new_list)
    print(travel_log_list)
    order = {
        "starter": {1: "Salad", 2: "Soup"},
        "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
        "dessert": {1: ["Ice Cream"], 2: []},
    }
    # print(order["main"][2][0])


# add_new_country("Russia",2,["Moscow","Saint Peter"])
import os
# secret auction program
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


from replit import clear


def Secret_Auction():
    Auction_Dictionary = {}
    stopInput = False
    while not stopInput:
        key_input = input("What is your name?: ")
        value_input = int(input("What is your bid?: $"))
        any_bid = input("Are there any other bidders? Type 'yes' or 'no'")
        if any_bid == 'no':
            stopInput = True
        else:
            clear()
        Auction_Dictionary[key_input] = value_input
    max_bid = list(Auction_Dictionary.values())[0]
    won_bid = {}
    for auc in Auction_Dictionary:
        if Auction_Dictionary[auc] > max_bid:
            won_bid[auc] = Auction_Dictionary[auc]
    print(f"The winner is {list(won_bid.keys())[0]} with a bid of ${list(won_bid.values())[0]} ")


#functions with outputs exercise
def TitleCaseFunc(firstname,lastname):
    """doc string - This is a way of adding command to a function, hover on this function calling u will see more"""
    #one way
    x = camelcase.CamelCase() #returns upper case as upper case
    #return x.hump(firstname+' '+lastname)
    #another way
    return f"{firstname.title()} {lastname.title()}" #return as camelcase even if input is all upper case
#multiple return values
# first_Name = input("Enter your first name")
# last_Name = input("Enter your last name")
# print(TitleCaseFunc(first_Name,last_Name))

#calculator program Concepts(while loops,Flags and Recursion)
def Addition(a,b):
    return a+b
def Subtraction(a,b):
    return a-b
def Multiplication(a,b):
    return a*b
def Division(a,b):
    return a/b
operations = {
        "+": Addition,
        "-": Subtraction,
        "*": Multiplication,
        "/": Division
    }
from calenderArt import calender
def calculator():
    print(calender)
    num1 = float(input("what's the first number?: "))
    for symbols in operations:
        print(symbols)
    should_Continue = True #FLAGS
    while should_Continue: #WHILE
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation]
        result = function(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        YorN = input(f"Type 'y' to continue calculating with {result},or type 'n' to start new calculation: ")
        if YorN == 'n':
            should_Continue = False
            calculator() # RECURSION
        else:
            num1 = result

from blackjack import logo
from replit import clear
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
def calculate_Score(cards):
    """Take a list of cards and return the score calculated from the list """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
def compare(userScore,computerScore):
    if userScore == computerScore:
        return "Draw "
    elif computerScore == 0:
        return "Lose, Your opponent win with a Blackjack 😭"
    elif userScore == 0:
        return "win with a blackjack 😎"
    elif userScore > 21:
        return "You went over. you lose 😭"
    elif computerScore > 21:
        return "Opponent went over. you win 😎"
    elif computerScore > userScore:
        return "You lose 😭"
    else:
        return "You win 😎"
def Blackjack():
    print(logo)
    userStops = True
    user_cards = []
    computer_cards = []
    isGameOver = False
    computerScore=0
    userScore=0
    for _ in range(2): #initially give 2 cards each
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not isGameOver:
        userScore = calculate_Score(user_cards)
        computerScore = calculate_Score(computer_cards)

        print(f"Your Cards:{user_cards}, current score:{userScore}")
        print(f"Computer's first card:{computer_cards[0]}")

        if userScore ==0 or computerScore == 0 or userScore > 21: # 0 indicates blackjack
            isGameOver = True
        else:
            userChoice = input("Type 'y' to get another card, type 'n' to pass: ")

            if userChoice == 'y':
                user_cards.append(deal_card())
            else:
                isGameOver = True

    while computerScore != 0 and computerScore < 17:
        computer_cards.append(deal_card())
        computerScore = calculate_Score(computer_cards)
    print(f"your final hand:{user_cards},fincal score:{userScore}")
    print(f"Computer's final hand: {computer_cards}, final score {computerScore}")
    print(compare(userScore,computerScore))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    Blackjack()
#scope concept
localvariable = 5
def increseValue():
    localvariable = 4
    print(f"my value is {localvariable}")

increseValue()
print(f"my value on the outside is {localvariable}")
# Secret_Auction()
from guessthenumber import logo
#number guessing game - use global variable concept
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def find_attempt(level):
    if level.lower() == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game !")
    print("I'm thinking of a number between 1 and 100")
    difficulty_Level = str(input("choose a difficulty. Type 'easy' or 'hard': "))
    computer_choice = random.randint(1,100)
    attemps_Left = find_attempt(difficulty_Level)
    while attemps_Left>0:
        print(f"You have {attemps_Left} attempts remaining to guess the number.")
        user_input = int(input("Make a guess: "))
        if computer_choice > user_input:
            print("Too Low")
            attemps_Left -= 1
        elif computer_choice < user_input:
            print("Too high")
            attemps_Left -= 1
        else:
            print(f"You got it! the answer was {computer_choice}")
            attemps_Left = 0


number_guessing_game()