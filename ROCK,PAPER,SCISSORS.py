import random

# Rock wins against Scissors
# Scissors wins against Paper
# Paper wins against Rock

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))


random_number = random.randint(0, 2)
print(type(choice), type(random_number))
print(f"The computer has chosen {random_number}")
if choice == random_number:
    print("It's a draw.")
elif choice == 0 and random_number == 2:
    print("You Win!")
elif choice == 1 and random_number == 0:
    print("You Win!")
elif choice == 2 and random_number == 1:
    print("You Win!")
elif int(choice) < 0 and int(choice) > 2:
    print("You typed an invalid number,you lose!")
else:
    print("You Lose!")

