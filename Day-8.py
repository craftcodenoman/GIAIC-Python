# 📢 Day 8 – Daily Python Challenge 🐍  

# 🚀 Challenge: 
# Aaj ka challenge "Number Guessing Game" hai! 🎯 Tumhe ek Python program 
# likhna hai jo ek random number (1-100) generate kare aur user ko us number ko guess karne ka chance de! 💡🔢  

# 🔥 Requirements: 
# 1️⃣ Random number generate karein (1-100 ke beech).
# 2️⃣ User se guess input lein.  
# 3️⃣ Agar guess sahi ho to "Congratulations! You guessed it right!" print karein. 
# 4️⃣ Agar galat ho to batao ke number chhota hai ya bada.  
# 5️⃣ User ko multiple attempts milne chahiye.

import random
def computer_guess():
    print("🎯 Welcome to the Computer Guess the Number Game! 🎯")
    print("Think of a number between 1 and 100, and I'll try to guess it.")

    low, high = 1, 100
    attempts = 0

    while True:
        guess = random.randint(low, high)  # Computer makes a guess
        attempts += 1

        # Ask the user for feedback
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").strip().lower()

        if feedback == 'h':
            high = guess - 1  # Adjust the upper bound
        elif feedback == 'l':
            low = guess + 1  # Adjust the lower bound
        elif feedback == 'c':
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts! 🎉")
            break
        else:
            print("⚠️ Invalid input! Please enter 'H' for too high, 'L' for too low, or 'C' for correct.")

# Run the game
computer_guess()