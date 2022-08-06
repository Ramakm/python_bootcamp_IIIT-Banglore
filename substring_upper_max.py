'''Description:
Given a string, write a Python program to find the largest substring of uppercase characters and print the length of that substring. Check the sample inputs and outputs for a better understanding.
---------------------------------------------------------------------------------------------------
Input - String

Output - String
---------------------------------------------------------------------------------------------------
Sample Input - I lovE PRogrAMMING

Sample Output - 6
'''

test_str = input()
upper = 0
max_upper = []

for i in test_str:
    if i.isupper():
        upper += 1 
        max_upper.append(upper)
    else:
        upper = 0
print(max(max_upper))
