logo = r'''
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

def auction_winner(complete_auction):
    highest_bid = 0
    winner = ""
    for bidder in complete_auction:
        if complete_auction[bidder] > highest_bid:
            highest_bid = complete_auction[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)
auction_continue = True
auction = {}
while auction_continue:
    name = input("What is your name? ")
    bid = int(input("What it your bid? $"))
    auction[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if other_bidders == "no":
        auction_continue = False
        auction_winner(auction)
    else:
        print("\n" * 20)
