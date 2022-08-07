'''Description:
Given an integer ‘n’, your task is to write a Python code to find whether ‘n’ is divisible by all its digits or not. If they divide the number, then the number ‘n’ is a happy number. Otherwise, it is a sad number.
The number ‘n’ may be provided with commas. At first, you have to clean the number (by removing the commas involved) and then check whether the number is happy or sad.
---------------------------------------------------------------------------------------------------
Input - String
Output - String
---------------------------------------------------------------------------------------------------
Sample Input - 2,128
Sample Output - Happy Number
--------------------------------------------------------------------------------------------------
Sample Input - 256
Sample Output - Sad Number '''

n = input()
x = n.replace(',','')
flag = True

for i in x:
    if int(i)!=0 and int(x)%int(i)==0:
        flag = True
    else:
        flag = False
        break
if flag:
    print('Happy Number')
else:
    print('Sad Number')