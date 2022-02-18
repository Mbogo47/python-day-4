import random
#.randit()-Generates random whole numbers
random_integer = random.randint(1,10)
print(random_integer)

#random.random -Returns the next random floating point number between 0 and 1
random_float=random.random()
print(random_float)

#To generate random float numbers between 0-5 you multiply the random float by 5
#instead of the love calculator
love_score = random.randint(1,100)
print(f"Your love score is {love_score}")
