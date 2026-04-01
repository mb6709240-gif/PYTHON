import random

print("🎲 Welcome to Dice Game – Player vs Computer!")

# Player rolls dice
input("Press Enter to roll your dice...")
player_roll = random.randint(1, 6)
print("You rolled:", player_roll)

# Computer rolls dice
computer_roll = random.randint(1, 6)
print("Computer rolled:", computer_roll)

# Determine winner
if player_roll > computer_roll:
    print("🎉 You win!")
elif player_roll < computer_roll:
    print("💻 Computer wins!")
else:
    print("🤝 It's a tie!")
