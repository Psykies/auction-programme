from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

biiding_record = {}


exit_loop = False

def higgest_bidder():
  highest_bid = 0
  winner = ""
  for bidder in biiding_record:
    bidding_amount = biiding_record[bidder]
    if  bidding_amount > highest_bid:
      highest_bid = bidding_amount
      winner = bidder
  print(f"The winner is {winner} and the item is sold for {highest_bid}")    
    
    
while exit_loop == False:
  name = input ("enter the bidders name ")
  bid = int(input("Enter yor bid "))
  biiding_record[name] = bid
  next_bidder = input("is there any more bidder 'yes' or 'no' :" )
  if next_bidder == "no":
    exit_loop= True
    clear()
    print(logo)
  else:
    clear()
    print(logo)

higgest_bidder()


