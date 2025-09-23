import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def blackjack():
    user_cards = []
    computer_cards = []

    print("\n" * 20)
    print(art.logo)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append((deal_card()))

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f"    Your cards: {user_cards}, current score: {user_score}")
    print(f"    Computer's first card: [{computer_cards[0]},?]")

    if computer_score == 21:
        print(f"    Your final hand: {user_cards}, final score: {user_score}")
        print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("Computer won with Blackjack! 😫")
    elif computer_score == 21:
        print(f"    Your final hand: {user_cards}, final score: {user_score}")
        print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
        print("User won with a Blackjack! 😁")
    else:
        another_card = "y"
        while another_card == "y":
            another_card = input("type 'y' to get another card, type 'n' to pass: ")
            if another_card == 'y':
                user_cards.append(deal_card())
                user_score = sum(user_cards)
                if user_score > 21 and 11 in user_cards:
                    index = user_cards.index(11)
                    user_cards[index] = 1
                    user_score = sum(user_cards)
                elif user_score > 21:
                    print(f"    Your final hand: {user_cards}, final score: {user_score}")
                    print(f"    Computer's final hand: [{computer_cards[0]},?]")
                    print("You Went over. You lose 😭")
                    return
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            print(f"    Computer's first card: [{computer_cards[0]},?]")

        while computer_score < 16:
            computer_cards.append(deal_card())
            computer_score = sum(computer_cards)

        if computer_score > 21 and 11 in computer_cards:
            index = computer_cards.index(11)
            computer_cards[index] = 1
            computer_score = sum(computer_cards)
        elif computer_score > 21:
            print(f"    Your final hand: {user_cards}, final score: {user_score}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("Computer went over. You win 😁")
            return

        if computer_score == user_score:
            print(f"    Your final hand: {user_cards}, final score: {user_score}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("Its a Draw 😑")
            return
        elif computer_score > user_score:
            print(f"    Your final hand: {user_cards}, final score: {user_score}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("You Lose 😓")
            return
        else:
            print(f"    Your final hand: {user_cards}, final score: {user_score}")
            print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
            print("You Win 😊")
            return

decision = input("Do you want to play a game of Blackjack? type 'y' or 'n':")

while decision == "y":

    blackjack()

    decision = input("Do you want to play a game of Blackjack? type 'y' or 'n':")

else:
    print("See you later! 🖖")