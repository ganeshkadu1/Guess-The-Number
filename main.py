from random import randint
from art import logo

random_number = randint(1,100)
print("Welcome to the Number Guessing Game!")
print(logo)
print("I'm thinking of a number between 1 to 100.")
level = input("Choose difficulty. Type 'easy' or 'hard': ")

def check_guess(user_input):
    if user_input == random_number:
      print(f"You Won 😃!! The answer was {random_number}")
      return True
    elif user_input < random_number:
        print ("Too Low")
        return False
    elif user_input > random_number:
        print ("Too high")
        return False

def play_game(life):
    correct_answer = False
    for i in range(0,life):
        if correct_answer:
            break
        else:
            print(f"You have {life-i} attempt remaining to guess the number")
            guess_number = int(input("Make a guess: "))
            correct_answer = check_guess(guess_number)
            if i==life-1:
                print(f"You Loose 😭!! The answer was {random_number}")
            else:    
               print("Guess Again !!!")

def check_input(level) : 
    while level == "easy" or level == "hard":
        if level.lower() == "easy":
          return 10
        elif level.lower() == "hard":
          return 5
        else:
            print("Check a input!!")
            level = input("Choose difficulty. Type 'easy' or 'hard': ")
        
life = check_input(level)
play_game(life)