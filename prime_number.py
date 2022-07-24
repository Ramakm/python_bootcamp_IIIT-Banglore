# Prime numbers are numbers that can only be cleanly divided by themselves and 1.
# https://en.wikipedia.org/wiki/Prime_number
# You need to write a function that checks whether if the number passed into it is a prime number or not.
# e.g. 2 is a prime number because it's only divisible by 1 and 2.
# But 4 is not a prime number because you can divide it by 1, 2 or 4.


def prime_checker(number):

    flag = True
    if number>1:
        for i in range(2, number): #2,3,4,5,6,7,8
            if number%i == 0:
                flag = False
                # print("It's not a prime number.")
                break
    if flag == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


    
n = int(input("Check this number: "))
prime_checker(number=n)
