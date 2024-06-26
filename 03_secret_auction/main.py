import os, art

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    print(art.gavel)
    print("Welcome to our new silent bid!")
    bids = {}
    keep_going = "yes"
    while keep_going == "yes":
        if len(bids) > 0: clear()
        name = input("Please enter your name:\n").title()
        price = 0
        while price <= 0:
            try:
                price = int(input("Now please enter your bid:\n$"))
            except:
                price = 0
        bids[name]=price
        if(len(bids)>=2):
            keep_going = ""
            while keep_going not in ("yes", "no"):
                print("Is there another bidder?")
                keep_going = input("yes/no:\n")

    highest_bid = 0
    winner = ""
    for bid in bids:
        bid_amount = bids[bid]
        if bid_amount > highest_bid:
            winner = bid
            highest_bid = bid_amount

    print(f"The winner is {winner} with a bid of ${highest_bid}")