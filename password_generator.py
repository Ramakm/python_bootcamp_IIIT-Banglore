#Instructions:

#generate a simple or hard password randomly by computer. Its should be a mix of captial,small letter, number and special symbols.
#Normal Password: 4 letters, 3 number, 1 special symbol
#Hard password: 4-8 letters, 4 numbers, 3 special symbols

#Use randommodule to create them randomy.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password =""     #We can take list as well tuples but at the end we needed a string. Can do that using type conversion.

for i in range(1,nr_letters+1):          ### This will take from 1 to the input you have provided s range never consider the end value, so we need to add +1
    random_choice = random.choice(letters)
    password = password + random_choice

for j in range(1,nr_symbols+1):
    random_symobls = random.choice((symbols))
    password = password+random_symobls


for j in range(1,nr_numbers+1):
    random_numbers = random.choice((numbers))
    password = password+random_numbers


print(f"Your password is : {password}.")
