import time

# Text colors for the terminal
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

score = 0

# Welcome Banner
print("\n==========================================")
print(YELLOW + "   🌟 WELCOME TO THE PYTHON TRIVIA QUIZ 🌟" + RESET)
print("==========================================\n")
time.sleep(1)

# Question 1
answer1 = input("🌍 1. What is the capital of France? ")
print("Checking answer...")
time.sleep(1)

if answer1.lower().strip() == "paris":
    print(GREEN + "✅ Correct!" + RESET)
    score = score + 1
else:
    print(RED + "❌ Wrong! The answer is Paris." + RESET)

print("\n------------------------------------------\n")

# Question 2
answer2 = input("🗺️  2. How many continents are there? ")
print("Checking answer...")
time.sleep(1)

if answer2.strip() == "7":
    print(GREEN + "✅ Correct!" + RESET)
    score = score + 1
else:
    print(RED + "❌ Wrong! There are 7 continents." + RESET)

print("\n------------------------------------------\n")

# Question 3
answer3 = input("🪐 3. What planet is known as the Red Planet? ")
print("Checking answer...")
time.sleep(1)

if answer3.lower().strip() == "mars":
    print(GREEN + "✅ Correct!" + RESET)
    score = score + 1
else:
    print(RED + "❌ Wrong! It is Mars." + RESET)

print("\n------------------------------------------\n")

# Question 4
answer4 = input("🐍 4. What programming language are you learning right now? ")
print("Checking answer...")
time.sleep(1)

if answer4.lower().strip() == "python":
    print(GREEN + "✅ Correct!" + RESET)
    score = score + 1
else:
    print(RED + "❌ Wrong! You are learning Python." + RESET)

print("\n------------------------------------------\n")

# Question 5
answer5 = input("🌊 5. What is the largest ocean on Earth? ")
print("Checking answer...")
time.sleep(1)

if answer5.lower().strip() == "pacific" or answer5.lower().strip() == "pacific ocean":
    print(GREEN + "✅ Correct!" + RESET)
    score = score + 1
else:
    print(RED + "❌ Wrong! It is the Pacific Ocean." + RESET)

# Final Results
print("\n==========================================")
print("Calculating your final score...")
time.sleep(1.5)
print(YELLOW + "🏆 Game over! Your final score is:", score, "out of 5" + RESET)

if score >= 4:
    print(GREEN + "🔥 Amazing job! You are a trivia master!" + RESET)
else:
    print("👍 Good effort! Run the game again to beat your score.")
print("==========================================\n")