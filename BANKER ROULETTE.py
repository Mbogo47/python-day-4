import random

name_string=input("Give me everybody's names, seperated by a comma.\n")
names = name_string.split(",")
print(names)

#Get the total number of items in a list using len() function

num_names = len(names)

random_choice=random.randint(0,num_names-1)

person_who_will_pay=names[random_choice]
print(person_who_will_pay + " is going to pay today")
#  print(random.choice(names) + " is going to be paying today")

# dirty_dozen=["Strawberries","Spinach","Kale","Nectarines","Apples","Grapes","Peaches","Cherries","pears","Tomatoes","Celery","Potatoes"]
fruits=["Strawberries","Nectarines","Apples","Grapes","Peaches","Cherries","pears"]
vegetables=["Spinach","Kale""Tomatoes","Celery","Potatoes"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen)


# HEAD OR TAIL GEN
import random

random_number = random.randint(1, 2)
print(random_number)

if random_number == 1:
    print("Heads")
else:
    print("Tails")

counties_in_kenya=["Muranga","Mombasa","Lamu","Nairobi", "Kirinyaga", "Meru", "Garissa","Turkana","Baringo","Kisumu"]

print(counties_in_kenya[-10])