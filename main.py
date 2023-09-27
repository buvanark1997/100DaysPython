# tip calculation program
import random
import camelcase
from caeserArt import logo
import os
from calenderArt import calender
from blackjack import logo
from replit import clear
from guessthenumber import logo
from higherlowergame_data import data
from higherlowerart import logo
from higherlowerart import vs


def calculate_tip():
    print("Welcome to the tip calculator")
    total_bill = float(input("What was the total bill?"))
    tip_percentage = int(input("What percentage tip would you like to give ?"))
    people = int(input("How many people to split the bill?"))

    tip_value = round(total_bill, 2) * (tip_percentage / 100)
    share = (tip_value + total_bill) / people
    formatted_share = "{:.2f}".format(share)  # it will print the last value even if its "0"
    print(f"Each person should pay: {round(share, 2)}")  # if last digit is "0" round will not print 0
    print(f"Each person should pay: {formatted_share}")


def order_pizza():
    print("Welcome to python pizza deliveries !")
    size = str(input("Enter pizza size. S, M or L?"))
    add_on = str(input("Do you need pepperoni on top? Y or N"))
    ex_cheese = str(input("Do you need extra cheese on top? Y or N"))
    price = 0
    if size.lower() == 's':
        price += 15
        if add_on.lower() == 'y':
            price += 2
    elif size.lower() == 'm':
        price += 20
        if add_on.lower() == 'y':
            price += 3

    elif size.lower() == 'l':
        price += 25
        if add_on.lower() == 'y':
            price += 3

    if ex_cheese.lower() == 'y':
        price += 1

    print(f"Your final bill is: ${price}")


def love_calculator():
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
    final_value = str(first_digit) + str(second_degit)
    if int(final_value) < 10 or int(final_value) > 90:
        message = f"Your score is {final_value}, you go together like coke and mentos"
    elif 40 <= int(final_value) <= 50:
        message = f"Your score is {final_value}, you are alright together"
    else:
        message = f"Your score is {final_value}"

    print(message)


# get random number from the computer which is not decided from us

def random_exercise():
    print(random.randint(1, 10000))
    print(random.random())


# program to pick random value from the list
def pa_bills():
    input_str = input("Enter list of names \n")
    list_names = input_str.split(",")
    length = len(list_names)
    random_value = random.randint(0, length - 1)
    print(f"{list_names[random_value]} is going to pay for the meal")


def combining_list():
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]
    list_combined = [list1, list2]
    print(list_combined[0][0])


def treasure_map():
    row1 = ["😏", "😏", "😏"]
    row2 = ["😏", "😏", "😏"]
    row3 = ["😏", "😏", "😏"]
    row = [row1, row2, row3]
    index_value = input(
        "Enter the index to mark")  # first digit represents column position second represents row position
    row_value = int(index_value[1]) - 1
    col_value = int(index_value[0]) - 1
    row[row_value][col_value] = "X"
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
    choice_array = ["rock", "paper", "scissors"]
    compute_choice = choice_array[random.randrange(0, len(choice_array) - 1)]
    print("Computer choice")
    if compute_choice == "rock":
        print(rock)
    elif compute_choice == "paper":
        print(paper)
    else:
        print(scissors)

    if your_choice == 0 and compute_choice.lower() == "scissors":
        print("You win")
    elif your_choice == 0 and compute_choice.lower() == "paper":
        print("You lose")
    elif your_choice == 2 and compute_choice.lower() == "rock":
        print("You lose")
    elif your_choice == 2 and compute_choice.lower() == "paper":
        print("You win")
    elif your_choice == 1 and compute_choice.lower() == "rock":
        print("You win")
    elif your_choice == 1 and compute_choice.lower() == "scissors":
        print("You lose")
    else:
        print("Draw")


# find the highest score from the list without using in-build functions

def highest_score():
    score_list_str = input("Enter list of scores: ")
    score_list = score_list_str.split(',')
    max_score = 0
    for i in score_list:
        if int(i) > max_score:
            max_score = int(i)

    print(max_score)


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


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to the PyPassword Generator!")
    generated_password = ""
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    for i in range(0, nr_letters):
        random_value = random.randint(0, len(letters) - 1)
        generated_password += letters[random_value]
    for i in range(0, nr_symbols):
        random_value = random.randint(0, len(symbols) - 1)
        generated_password += symbols[random_value]
    for i in range(0, nr_numbers):
        random_value = random.randint(0, len(numbers) - 1)
        generated_password += numbers[random_value]
    generated_password = list(generated_password)
    generated_password = random.sample(generated_password, len(generated_password))
    generated_password = ''.join(generated_password)  # to convert list to string
    print(f"Here is your password: {generated_password}")


def hangman_exercise_1():
    words = ['Moon', 'ISRO', 'VikramLander']
    selected_word = random.choice(words)
    ic = input("Enter letter")
    for c in selected_word:
        if ic.lower() == c.lower():
            print("Right")
        else:
            print("Wrong")


def hangman_exercise_2():
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
    selected_word = random.choice(words)
    print(selected_word)
    blank_word = ""
    lives = 6
    for l in selected_word:
        blank_word += "_"
    while lives > 0:
        ic = input("Enter letter")
        for i in range(0, len(selected_word)):
            if ic.lower() == selected_word[i].lower():
                blank_word = list(blank_word)
                blank_word[i] = ic
        print(''.join(blank_word))
        if ic not in selected_word:
            lives = lives - 1

            if lives == 0:
                print("You Lose")

    if '_' not in blank_word:
        print("You Won")
    print(stages[lives])


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesercipher():
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    secret_message = ""
    while shift > 52:
        shift = shift % len(alphabet)
    for t in text:
        if t.isalpha():
            index = alphabet.index(t)
            if direction == 'encode':
                index += shift
            else:
                index -= shift
            append_msg = alphabet[index]
        else:
            append_msg = t
        secret_message += append_msg

    print(f" your {direction}d message is {secret_message}")


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Heroine": 99,
    "Draco": 74,
    "Neville": 62
}


# Dictionary
def find_result():
    result_student = {}
    for stu in student_scores:
        if student_scores[stu] >= 91:
            result_student[stu] = "Outstanding"
        elif 81 <= student_scores[stu] <= 90:
            result_student[stu] = "Exceeds Expectations"
        elif 71 <= student_scores[stu] <= 80:
            result_student[stu] = "Acceptable"
        else:
            result_student[stu] = "Fail"

    print(result_student)


# nesting dictionary in a dictionary
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


def add_new_country(country, no_of_visits, cities_list):
    new_list = {
        "Country": country,
        "Cities_visited": cities_list,
        "Total_visits": no_of_visits
    }
    travel_log_list.append(new_list)
    print(travel_log_list)
    # print(order["main"][2][0])


# add_new_country("Russia",2,["Moscow","Saint Peter"])


# secret auction program
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def secret_auction():
    auction_dictionary = {}
    stop_input = False
    while not stop_input:
        key_input = input("What is your name?: ")
        value_input = int(input("What is your bid?: $"))
        any_bid = input("Are there any other bidders? Type 'yes' or 'no'")
        if any_bid == 'no':
            stop_input = True
        else:
            clear()
        auction_dictionary[key_input] = value_input
    max_bid = list(auction_dictionary.values())[0]
    won_bid = {}
    for auc in auction_dictionary:
        if auction_dictionary[auc] > max_bid:
            won_bid[auc] = auction_dictionary[auc]
    print(f"The winner is {list(won_bid.keys())[0]} with a bid of ${list(won_bid.values())[0]} ")


# functions with outputs exercise
def title_case_func(firstname, lastname):
    """doc string - This is a way of adding command to a function, hover on this function calling u will see more"""
    # one way
    x = camelcase.CamelCase()  # returns upper case as upper case
    # return x.hump(firstname+' '+lastname)
    # another way
    return f"{firstname.title()} {lastname.title()}"  # return as camelcase even if input is all upper case


# multiple return values
# first_Name = input("Enter your first name")
# last_Name = input("Enter your last name")
# print(TitleCaseFunc(first_Name,last_Name))

# calculator program Concepts(while loops,Flags and Recursion)
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}


def calculator():
    print(calender)
    num1 = float(input("what's the first number?: "))
    for symbols in operations:
        print(symbols)
    should_continue = True  # FLAGS
    while should_continue:  # WHILE
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        function = operations[operation]
        result = function(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        y_or_n = input(f"Type 'y' to continue calculating with {result},or type 'n' to start new calculation: ")
        if y_or_n == 'n':
            should_continue = False
            calculator()  # RECURSION
        else:
            num1 = result
            
            
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the list """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw "
    elif computer_score == 0:
        return "Lose, Your opponent win with a Blackjack 😭"
    elif user_score == 0:
        return "win with a blackjack 😎"
    elif user_score > 21:
        return "You went over. you lose 😭"
    elif computer_score > 21:
        return "Opponent went over. you win 😎"
    elif computer_score > user_score:
        return "You lose 😭"
    else:
        return "You win 😎"


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    computer_score = 0
    user_score = 0
    for _ in range(2):  # initially give 2 cards each
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your Cards:{user_cards}, current score:{user_score}")
        print(f"Computer's first card:{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:  # 0 indicates blackjack
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"your final hand:{user_cards},fincal score:{user_score}")
    print(f"Computer's final hand: {computer_cards}, final score {computer_score}")
    print(compare(user_score, computer_score))


# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
# clear()
# Blackjack()
# scope concept
local_variable = 5


def increase_value():
    local_variable = 4
    print(f"my value is {local_variable}")


increase_value()
print(f"my value on the outside is {local_variable}")
# Secret_Auction()


# number guessing game - use global variable concept
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
    difficulty_level = str(input("choose a difficulty. Type 'easy' or 'hard': "))
    computer_choice = random.randint(1, 100)
    attempts_left = find_attempt(difficulty_level)
    while attempts_left > 0:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        user_input = int(input("Make a guess: "))
        if computer_choice > user_input:
            print("Too Low")
            attempts_left -= 1
        elif computer_choice < user_input:
            print("Too high")
            attempts_left -= 1
        else:
            print(f"You got it! the answer was {computer_choice}")
            attempts_left = 0


# higher lower game - self coding ex
def higher_lower_game():
    print(logo)
    user_failed = False
    user_score = 0
    option_b = random.choice(data)
    while not user_failed:
        option_a = option_b
        option_b = random.choice(data)
        if option_a == option_b:
            option_b = random.choice(data)
        print(f"Compare A:{option_a['name']}, {option_a['description']}, from {option_a['country']}")
        print(vs)
        print(f"Against B:{option_b['name']}, {option_b['description']}, from {option_b['country']}")
        user_choice = input("Who has more followers? Type 'A' or 'B'")
        if option_a['follower_count'] > option_b['follower_count'] and user_choice.lower() == 'a':
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        elif option_a['follower_count'] < option_b['follower_count'] and user_choice.lower() == 'b':
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            user_failed = True




