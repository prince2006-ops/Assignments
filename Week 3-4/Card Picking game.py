import random
cards_list=['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
suits_list=['Heart','Diamond','Spades','Club']
random_card=random.choice(cards_list)
random_suit=random.choice(suits_list)

user_card_list=input("Enter the card choice:").strip().capitalize()
user_suit_list=input("Enter the suit list:").strip().capitalize()
if (user_card_list not in cards_list) and(int(user_card_list)<2 or int(user_card_list)>10):
    print("Please choose the correct choice")
    quit()
elif user_suit_list not in (suits_list):
    print("The suit is invalid")
    quit()

if (random_card==user_card_list) and (random_suit==user_suit_list):
    print("Congratulations! Your choice is correct❤️😊")
else:
    print(" 💔Game Over!")

print(f"The choice of computer was {random_suit} of {random_card}")
