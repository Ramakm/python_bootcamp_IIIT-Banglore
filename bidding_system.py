#Ask user to enter names and bids 
#Enter those entires in a new dictionary as key and values.
#Ask user to whether new bidders are available or not. If new bidder available then ask then to enter their name and bids and add them to the dictionay
#Find the maximum bidding value of the dictionary.
#You can add a logo here of a bidding machine. Clear() can be used once one person details has been included if another one is present.



logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")


user ="Yes"
dict= {}
while user == "Yes":
  name = input("Enter Name: ")
  bid_price = int(input("enter Bid price: "))
  dict.update({name:bid_price})
  print(dict)
  user = input("Other Users with bid avialable: Yes or No\n")
  clear()

highest_bidder(dict)

