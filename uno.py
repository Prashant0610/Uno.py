
# Programme Starts #
import random


# Defining Functions
def distribution_card(hand_1, hand_2, deck_of_card):
    card_dis = 0
    while card_dis < 7:
        hand_1.append(deck_of_card[0])
        deck_of_card.pop(0)
        hand_2.append(deck_of_card[0])
        deck_of_card.pop(0)
        card_dis += 1

    return hand_1, hand_2, deck_of_card


def card_see(hand):
    list_c = []
    for crd_ in hand:
        card_c = f"{crd_[0]} Of {crd_[1]}"
        list_c.append(card_c)

    return list_c


def card_addition(hand, number_card, deck_of_card):
    for c in range(number_card):
        hand.append(deck_of_card[0])
        deck_of_card.pop(0)

    return hand, deck_of_card


# Rules
print("""This is the UNO game
Card Format: "RANK" of "Color"
Rules: 
>>> Give a card with same Rank or Color
>>> Write "DRAW" to pick a card form deck(Note: 'Draw' should be written with correct spelling, else the program will crash)
>>> After picking a card , You turn ENDS
>>> Successive +4 or +2 Cards are not allowed
>>> +4 and 'Wild' Gives you a chance to change color(Note: Spelling of colors should be written properly(color: red, blue, green, yellow))
>>> The one who play all his card WINS THE GAME 
>>> DON'T TYPE WRONG INPUTS(The programme will CRASH)
ENJOY!!!!""")
# Making The Deck
deck = []
user_hand = []
computer_hand = []
ranks = ["0"] + ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "+2"] * 2
colors = ["Blue", "Red", "Yellow", "Green"]
special = ["+4"] * 4 + ["Wild"] * 4
for color in colors:
    for rank in ranks:
        card = [rank, color]
        deck.append(card)

for sp in special:
    card_s = [sp, "Special"]
    deck.append(card_s)

# The Game
random.shuffle(deck)
while len(deck) >= 0:
    card_top = deck[0]
    deck.remove(card_top)
    user_hand, computer_hand, deck = distribution_card(user_hand, computer_hand, deck)
    print(f"Card: {card_top[0]} of {card_top[1]}")
    while len(user_hand) != 0 and len(computer_hand) != 0:
        # Defining User Turn And Rules
        user_turn = True
        print("" * 45 + " Your Turn " + "" * 45)
        while user_turn:
            ucs = card_see(user_hand)
            print(ucs)
            u_index = input("Give the position of your card: ")
            if u_index.lower() == "draw":
                user_hand.append(deck[0])
                deck.pop(0)
                user_turn = False

            else:
                user_throw = user_hand[int(u_index) - 1]
                if user_throw[0] == card_top[0] or user_throw[1] == card_top[1]:
                    if user_throw[1] == "Special":
                        if user_throw[0] == "Wild":
                            print(f"Your Card: {user_throw[0]} Of {user_throw[1]}")
                            color_chosen = input("Give the color: ")
                            print(f"Color changes to {color_chosen}")
                            card_top[0] = "Wild"
                            card_top[1] = color_chosen.title()
                            user_hand.remove(user_throw)
                            user_turn = False

                        else:
                            computer_hand, deck = card_addition(computer_hand, 4, deck)
                            print(f"Your Card: {user_throw[0]} Of {user_throw[1]}")
                            color_chosen = input("Give the color: ")
                            print(f"Color changes to {color_chosen}")
                            card_top[0] = "+4"
                            card_top[1] = color_chosen.title()
                            user_hand.remove(user_throw)
                            print("Computer draw's 4 cards from deck")
                            computer_turn = False

                    elif user_throw[0] == "Skip" or user_throw[0] == "Reverse":
                        print(f"Your Card: {user_throw[0]} Of {user_throw[1]}")
                        card_top = user_throw
                        user_hand.remove(user_throw)
                        computer_turn = False

                    elif user_throw[0] == "+2" and user_throw[1] == card_top[1] and card_top[0] != "+2":
                        print(f"Your Card: {user_throw[0]} Of {user_throw[1]}")
                        computer_hand, deck = card_addition(computer_hand, 2, deck)
                        card_top = user_throw
                        user_hand.remove(user_throw)
                        print("Computer draw's 2 cards from deck")
                        computer_turn = False

                    elif card_top[0] == "+2" and user_throw[0] == "+2":
                        print(f"Your Card: {user_throw[0]} Of {user_throw[1]}")
                        computer_hand, deck = card_addition(computer_hand, 2, deck)
                        card_top = user_throw
                        user_hand.remove(user_throw)
                        print("Computer draw's 2 cards from deck")
                        computer_turn = False
                    else:
                        print(f"Your Card: {user_throw[0]} Of {user_throw[1]}")
                        card_top = user_throw
                        user_hand.remove(user_throw)
                        user_turn = False

                elif user_throw[1] == "Special":
                    if user_throw[0] == "Wild":
                        print(f"Your Card: {user_throw[0]} Of {user_throw[1]}")
                        color_chosen = input("Give the color: ")
                        print(f"Color changes to {color_chosen}")
                        card_top[1] = color_chosen.title()
                        user_hand.remove(user_throw)
                        user_turn = False

                    else:
                        computer_hand, deck = card_addition(computer_hand, 4, deck)
                        print(f"Your Card: {user_throw[0]} Of {user_throw[1]}")
                        color_chosen = input("Give the color: ")
                        print(f"Color changes to {color_chosen}")
                        card_top[1] = color_chosen.title()
                        user_hand.remove(user_throw)
                        print("Computer draw's 4 cards from deck")
                        computer_turn = False

                else:
                    print("Wrong Card Thrown")
                    print("Try Again")

        # Defining Computer Turn And Rules
        if len(user_hand) >= 1:
            computer_turn = True
        else:
            computer_turn = False
        print("" * 45 + " Computer Turn " + "" * 45)
        while computer_turn:
            card_valid = []
            for crd in computer_hand:
                if crd[0] == card_top[0] or crd[1] == card_top[1]:
                    card_valid.append(crd)

                elif crd[1] == "Special":
                    card_valid.append(crd)
            if len(card_valid) == 0:
                computer_hand.append(deck[0])
                deck.pop(0)
                computer_turn = False
                print("Computer draw's a card")

            else:
                comp_throw = card_valid[0]
                if comp_throw[0] == "+4":
                    user_hand, deck = card_addition(user_hand, 4, deck)
                    print(f"Computer Card: {comp_throw[0]} Of {comp_throw[1]}")
                    color_chosen = random.choice(colors)
                    print(f"Color changes to {color_chosen}")
                    card_top[1] = color_chosen.title()
                    computer_hand.remove(comp_throw)
                    print("4 Cards added to your hand")
                    user_turn = False

                elif comp_throw[0] == "+2":
                    user_hand, deck = card_addition(user_hand, 2, deck)
                    print(f"Computer Card: {comp_throw[0]} Of {comp_throw[1]}")
                    computer_hand.remove(comp_throw)
                    print("2 Cards added to your hand")
                    user_turn = False

                elif comp_throw[0] == "Wild":
                    print(f"Computer Card: {comp_throw[0]} Of {comp_throw[1]}")
                    color_chosen = random.choice(colors)
                    print(f"Color changes to {color_chosen}")
                    card_top[1] = color_chosen.title()
                    computer_hand.remove(comp_throw)
                    computer_turn = False

                elif comp_throw[0] == "Skip" or comp_throw[0] == "Reverse":
                    card_top = comp_throw
                    computer_hand.remove(comp_throw)
                    user_turn = False
                    print(f"Computer Card: {comp_throw[0]} Of {comp_throw[1]}")

                elif comp_throw[1] == card_top[1]:
                    card_top = comp_throw
                    computer_hand.remove(comp_throw)
                    computer_turn = False
                    print(f"Computer Card: {comp_throw[0]} Of {comp_throw[1]}")

                else:
                    card_top = comp_throw
                    computer_hand.remove(comp_throw)
                    computer_turn = False
                    print(f"Computer Card: {comp_throw[0]} Of {comp_throw[1]}")

    # Deciding The Winner
    if len(user_hand) == 0:
        print("HOORAY! You Won")
        break

    else:
        print("OPPS!!! You lost")
        print("Computer Won")
        break

# Defining A Tie
if len(deck) <= 0:
    print("OPPS!!! Cards in Deck are Exhausted")
    print("It's a Tie")
    print("Better Luck! Next Time")