import random
import art


def set_difficulty():
    dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if dif=='hard':
        return 5
    elif dif=="easy":
        return 10

def checker(num_guessed,ans_num):
    if num_guessed==ans_num:
        print(f"You got it the answer was {ans_num}.")
    elif num_guessed>ans_num:
        print("Too high.")
    else:
        print("Too low.")

def game():
    print(art.logo)
    print("I am thinking of a number between 1 and 100.")
    ans_num = random.randint(1, 100)
    life = set_difficulty()
    guess=0
    while guess!=ans_num:
        print(f"You have {life} lives.")
        guess=int(input("Make a guess: "))
        life-=1
        checker(guess,ans_num)

game()