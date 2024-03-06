from replit import clear
import blind_art
#HINT: You can call clear() to clear the output in the console.
print(blind_art.logo)
auction_dic = {}
bidding = True


def blind_auction():
    highest_bid = 0
    winner = ""
    for bidder in auction_dic:
    bid = auction_dic[bidder]
    winner = bidder
    if bid > highest_bid:
        highest_bid = bid
        winner = bidder
    print (f"the winner is {winner} with a bid of R$ {highest_bid}")

  
    while bidding == True:
        name = input("What is your name? ")
        bid = float(input("What is your bid? R$ "))
        auction_dic[name] = bid
        more = input("Are there any other bidders? yes or no? ").lower()
        if more == "no":
            clear()
            bidding = False
        else:
            clear()

blind_auction()
  

