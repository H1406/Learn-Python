from random import random
import os
os.system('cls')
card_dic = {
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "ten": "10",
    "J": "10",
    "Q": "10",
    "K": "10",
    "A": "11",
}
card_name = [
    "two",
    "two",
    "two",
    "two",
    "three",
    "three",
    "three",
    "three",
    "four",
    "four",
    "four",
    "four",
    "five",
    "five",
    "five",
    "five",
    "six",
    "six",
    "six",
    "six",
    "seven",
    "seven",
    "seven",
    "seven",
    "eight",
    "eight",
    "eight",
    "eight",
    "nine",
    "nine",
    "nine",
    "nine",
    "ten",
    "ten",
    "ten",
    "ten",
    "J",
    "J",
    "J",
    "J",
    "Q",
    "Q",
    "Q",
    "Q",
    "K",
    "K",
    "K",
    "K",
    "A",
    "A",
    "A",
    "A",
]
is_Continue = True
dealer_card = {"name": [], "value": []}
player_card = {"name": [], "value": []}
player_point = 0
dealer_point = 0
p_dealer_point = 0
p_busted = False
d_busted = False
is_drawCard = True


# bet_money = int(input("What's your bet?: $"))
def draw_card(card):
    global card_dic
    global card_name
    #score = 0
    player_ran = card_name[int(random() * len(card_name))]
    # for i in range(len(card["value"])):
    #     score += int(card["value"][i])
    # if player_ran == "A":
    #     if score > 10:
    #         card_dic.update({"A": 1})
    card["name"].append(player_ran)
    card["value"].append(card_dic[player_ran])

    return card


def cal_score(card,name):
    score = 0
    for i in range(len(card["value"])):
        temp= int(card["value"][i])
        if card["name"][i]=="A":
            if name == "player":
                if player_point>10:
                    temp = 1
            else: 
                if dealer_point>10:
                    temp = 1
        score += temp
    return score

player_draw_card=True

while is_Continue:
    if not p_busted and player_draw_card:
        player_card = draw_card(player_card)
        player_point = cal_score(player_card,"player")
        print(player_point)
        print(f"PlayerCard: {player_card['name']}")
    if (not d_busted) or is_drawCard:
        dealer_card = draw_card(dealer_card)
        dealer_point = cal_score(dealer_card,"dealer")
        print(f"DealerCard: {dealer_card['name']}")
    if player_point > 21:
        p_busted = True
    else:
        ask = input("Do you want to draw another card? y/n ")
        if ask.lower() == "n":
            player_draw_card=False
    if dealer_point > 21:
        d_busted = True
        break
    elif dealer_point >= player_point or p_busted:
        is_drawCard = False
    if len(player_card) == 2 and player_point == 21:
        print("Black Jack!!! You won!!!")
        break
    if len(dealer_card["name"]) == 2 and dealer_point == 21:
        print("Black Jack!!! You lost!!!")
        break
if player_point > dealer_point and not p_busted:
    print("You win!!!")
if player_point < dealer_point and d_busted and not p_busted:
    print("Win")
if player_point < dealer_point and not d_busted:
    print("Lose")
if d_busted and p_busted:
    print("Draw")
if dealer_point == player_point:
    print("Draw")
print(player_point)
print(player_card["name"])
print(dealer_point)
print(dealer_card["name"])
