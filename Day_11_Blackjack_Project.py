import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def results(dealer_final_hand, player_final_hand):
    """Checks the final score of player and dealer to determine the winner"""
    if sum(dealer_final_hand) > 21:
        print("The dealer has gone over. You win \U0001F600")
    elif sum(dealer_final_hand) == sum(player_final_hand):
        print("Your hands are equal. It's a draw \U0001F643")
    elif sum(dealer_final_hand) > sum(player_final_hand):
        print("Dealer wins \U0001F915")
    else:
        print("You win \U0001F600")

def current_score(dealer_cards, player_cards):
    """Displays the current score of game, not final score"""
    print(f"    Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"    Dealer's first card: {dealer_cards[0]}")

def deal(card, hand):
    """Converts ACEs to 1 if score >=11, deals a card to a hand list"""
    if sum(hand) >= 11 and card == 11:
        hand.append(1)
    else:
        hand.append(card)

def blackjack():
    """Initiates a game of blackjack"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print("\n" * 20)
    print(logo)

    dealer_hand = []
    player_hand = []

    for i in range(2):
        deal(random.choice(cards), dealer_hand)
        deal(random.choice(cards), player_hand)

    current_score(dealer_hand, player_hand)

    if sum(player_hand) == 21 and sum(dealer_hand) == 21:
        print("It's a draw, you both drew a blackjack! \U0001F643")
        return
    elif sum(player_hand) == 21:
        print("You win with a blackjack!\U0001F600")
        return
    elif sum(dealer_hand) == 21:
        print("Dealer drew a blackjack, you lose \U0001F915!")
        return

    deal_another_card = True
    while deal_another_card:
       player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
       if player_choice == "y":
           deal(random.choice(cards), player_hand)
           current_score(dealer_hand, player_hand)
           if sum(player_hand) > 21:
               print("You went over. You lose \U0001F915")
               return
       else:
           deal_another_card = False

    while sum(dealer_hand) < 17:
        deal(random.choice(cards), dealer_hand)

    print(f"    Your final hand: {player_hand}, final score: {sum(player_hand)}")
    print(f"    Dealer's final hand: {dealer_hand}, final score: {sum(dealer_hand)}")

    results(dealer_hand, player_hand)

play_blackjack = True

while play_blackjack:
    game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game_start == "y":
        blackjack()
    else:
        play_blackjack = False
