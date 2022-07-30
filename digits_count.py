# Description
# Write a program to accept a number from the user and count the zeros, odd digits and non-zero even digits from the entered number.
# Input:
# A positive integer of n digits
# Output:
# Three integers representing the occurrences of zeros, odd digits and non-zero even digits from the entered number.
# Sample input:
# 1030
# Sample output:
# Number of odd digits: 2
# Number of non-zero even digits: 0
# Number of zeros: 2

# Take input

n=int(input())
odd_digit = 0
even_digit = 0
zeros = 0
#write your code here
num = n
while num >0:
    reminder = num%10
    if (reminder is not 0) and (reminder%2 == 0):
        even_digit += 1
    elif reminder == 0:
        zeros += 1
    else:
        odd_digit += 1 
    num //= 10
print(f"Number of odd digits: {odd_digit}")
print(f"Number of non-zero even digits: {even_digit}")
print(f"Number of zeros: {zeros}")


