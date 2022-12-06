"""Integration game of 21 """
"""number game of 21 kinda like blackjack two"""
__author__ = " Salatheo Clay "

import random


def multiplicativeidentity(number_by_1):
    """
passes the parameter of whatever number is entered in numberby1
    param number_by_1:
    """

    number_times_1 = 1 * number_by_1
    print(number_times_1)


def calculate_taxes_on_pizza():
    """
defines the function calculate taxes on pizza where the tax is given and
the price of pizza is given
    """
    taxes = .06
    pizza_hut_pizza = 4.79
    tax_of_pizza = taxes * pizza_hut_pizza
    print("the tax of a personal pan pizza is", tax_of_pizza)


# uses the data held in main and assigns the answer to taxofpizza

def main():
    """
 calculates the tax of pizza for the first function
 Completes the multiplicative identity for the second function
    """
    number_by_1 = int(input('put in number to calculate the tax on pizza'))
    calculate_taxes_on_pizza()
    multiplicativeidentity(number_by_1)


main()
sep = ''
(9 * 9)
# multiplication
(9 / 9)
# division gets 1
(15 // 4)
# remainder division divides to the highest point without remainder
(15 % 4)
# modulus outputs the remainder of the quotient
("sal" + "atheo")
# adds 2 strings together end by end
("hello" * 3)
# prints hello 3 times
(9 != 5)
# boolean operator b=not and equal
for x in range(4, 1, -1):
    print("game starting in", x - 1)
# for function countdown the numbers from 3 by intervals of -1


game = True
if not game:
    print("game is true")
# not statement prints game is true if game was = False

name = input("what is your name")
name_2 = input("what is player two's name")
print("hello", name, "and", name_2)
print("today you will be playing a game of 21", name, "and", name_2)
print("you will be playing against a friend")
print("you and the other player will draw a number")
print("the goal is to be the closest to the number 21 without going over")

player_total_1 = 0
player_total_2 = 0
hitvalue = 0
hitvalue2 = 0
answer_evaluate = True
answer_evaluate2 = True
player_continue_confirmation = False
player_continue_confirmation2 = False

while answer_evaluate:
    # loop that determines if answer is valid or not
    player_continue = input(
        "Enter yes if you would like to begin player 1 ")
    if player_continue == "yes":
        answer_evaluate = False
        # boolean operator == is used meaning  player continue equals yes
        player_continue_confirmation = True
    # if statement that when entered yes while player can play the game
    else:
        answer_evaluate = True
        print("invalid response")

while player_continue_confirmation:

    player_continue = input("Enter yes if you would like to hit,no to stop")
    if player_continue == "yes":
        hitvalue += random.randrange(1, 11)
        player_total_1 += hitvalue
        print(name, "your hit value was", hitvalue)
        print(name, "your new player total is", player_total_1)

        player_continue_confirmation = True
    # when no is entered the loop ends
    elif player_continue == "no":
        player_continue_confirmation = False
    else:
        print("please enter yes for another hit, no to stop")
        #anything besides yes or no will not be accepted
answer_evaluate2 = True
player_continue_confirmation2 = False
while answer_evaluate2:
    # loop that determines if answer is valid or not
    player_continue2 = input(
        "Enter yes if you would like to begin, no to stop, player 2")
    if player_continue2 == "yes":
        answer_evaluate2 = False
        # boolean operator == is used meaning  player continue equals yes
        player_continue_confirmation2 = True
    # if statement that when entered yes while player can play the game
    elif player_continue2 == "no":
        player_continue_confirmation2 = False
        answer_evaluate = False
    else:
        print("invalid response")
        answer_evaluate2 = True
print("it is now your turn", name_2)
while player_continue_confirmation2:
  player_continue2 = input("Enter yes if you would like a hit no to stop")

  if player_continue2 == "yes":
        hitvalue2 += random.randrange(1, 11)
        player_total_2 += hitvalue2
        print("your hit value was", hitvalue2)
        print("your new player total is", player_total_2)
        player_continue_confirmation2 = True
  elif player_continue2 == "no":
      player_continue_confirmation2 = False
  else:
      print("invalid answer try again")

print(name, " final playertotal was", player_total_1)
print(name_2, "final playertotal was", player_total_2)
# being added to player total
# fix addition to player score
# if statements evaluate player total compares to other player and 21
# awards winner
if player_total_2 < player_total_1 < 21:
    print(name, "wins congrats!")

elif player_total_1 < player_total_2 < 21:
    print(name_2, "wins congrats!")

elif player_total_1 > 21 > player_total_2:
    print(name_2, "wins congrats")

elif player_total_1 < 21 < player_total_2:
    print(name, "congrats")

elif player_total_1 == player_total_2:
    print(name, "and", name_2, "draw")
elif player_total_1 and player_total_2> 21:
   print("no one wins")

print("thanks for playing", end=' have a nice day')
