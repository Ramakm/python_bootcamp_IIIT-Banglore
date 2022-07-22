# Instructions:

# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#name1 = "Angela Yu"

#name2 = "Jack Bauer"

comb_name1 = name1+name2
comb_name = comb_name1.lower()

t = comb_name.count("t")
r = comb_name.count("r")
u = comb_name.count("u")
e = comb_name.count("e")
l = comb_name.count("l")
o = comb_name.count("o")
v = comb_name.count("v")
e = comb_name.count("e")

true = t+r+u+e
love = l+o+v+e

love_score = int(str(true) + str(love))

if love_score<10 or love_score>90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score>=40 and love_score<=50:
  print(f"Your score is {love_score}, you are alright together.")

else:
  print(f"Your score is {love_score}.")