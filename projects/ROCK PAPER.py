# cook your dish here
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    print("🎮 Rock, Paper, Scissors Game")  
    while True:
        try:
            user_choice = input("\nEnter rock, paper, or scissors (or 'q' to quit): ").lower()
        except EOFError:
            # Handle the case where input stream closes unexpectedly
            print("\nInput stream closed. Exiting game.")
            break
        if user_choice == 'q':
            print("Thanks for playing!")
            break
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Try again!")
            continue
        computer_choice = get_computer_choice()
        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}"
        result = get_winner(user_choice, computer_choice)
        print(result)
# Run the game
play_game()
