#salatheo clay 
# number game of 21 kinda like blackjack 
#two players
def multiplicativeidentity(numberby1):
#passes the parameter of whatever number is entered in numberby1
   numberTimes1= 1*numberby1
   print(numberTimes1)
def calculateTaxesonPizza():
     taxes= .06
     pizzaHutPizza=4.79
     taxOfpizza= taxes*pizzaHutPizza
     print("the tax of a personal pan pizza is",taxOfpizza)
    #uses the data held in main and assigns the answer to taxofpizza
   
def main():
     numberby1= int(input("put in number to calculaye the tax on pizza"))
     calculateTaxesonPizza()
     multiplicativeidentity(numberby1)
     
    
     #function that determines the tax of pizza
     
main()
sep= ''
(9*9)
  #multiplation
(9/9)
  #divison gets 1
(15//4)
#remaindor divison divides to the highest point without remainder
(15%4)
#modulus outputs the remainder of the quotient 
("sal"+"atheo")
#adds 2 strings together end by end
("hello"*3)
#prints hello 3 times
(9!=5)
#boolen operator b=not and equal
for x in range(4,1,-1):
    print ("game starting in",x-1)
#for function countsdown the numbers from 3 by intervals of -1
game= True
if not game :
    print("game is true")
#not statement prints game is true if game was = False
    
name = input("what is your name")
name2= input("what is player two's name")
print ("hello", name, "and" ,name2)
print("today you will be playing a game of 21", name ,"and" ,name2)
print ("are you ready to begin")
#try if statement to start game with a yes input
print ("you will be playing against a friend")
print("you and the other player will draw a number")
print ("the goal is to be the closest to the numberer 21 without going over vs your friend")
print ("lets begin", name)

import random
playertotal1=0
playertotal2=0
hitvalue=0
hitvalue2=0


player_continue_confirmation= True
#if statemtn that when entered yes while player can play the game 
playercontinue =input("Enter yes if you would like your first hit player1")
if playercontinue == "yes":
    # boolen operator == is used meaning  playercontiue equals yes
   player_continue_confirmation= True
   while player_continue_confirmation:
  
     hitvalue+= random.randrange(1,12)
     playertotal1+= hitvalue
     print("your hit value was", hitvalue)
     print("your new player total is", playertotal1)
     playercontinue =input("Enter yes if you would like another hit, no to stop")
     if playercontinue !="no":
          print("invalid answer try again")
         playercontinue= input("Enter yes if you would like another hit, no to stop")
     # when no is entred the loop ends
     if playercontinue== "no":
         player_continue_confirmation= False
playercontinue2 =input("Enter yes if you would like your first hit player 2, other to stop")
if playercontinue2 == "yes":
   player_continue_confirmation2= True
   while player_continue_confirmation2:
  
     hitvalue2+= random.randrange(1,12)
     playertotal2+= hitvalue
     print("your hit value was", hitvalue)
     print("your new player total is", playertotal2)
     playercontinue2 =input("Enter yes if you would like another hit, no to stop")
     if playercontinue2 == "no":
         player_continue_confirmation2= False
     if playercontinue2 !="no":
          print("invalid answer try again")
         playercontinue2= input("Enter yes if you would like another hit, no to stop")


print (playertotal1)
#visual toatal of player count after being added to with random number 



print (name, " final playertotal was" ,playertotal1)
print (name2, "final playertotal was" ,playertotal2)
#being added to player total
#fix addition to player score
#if statements evaluate player total compared to other pkayer and 21 and awards winner
if playertotal1>playertotal2 and playertotal1<21:
        print(name1, "wins congrats!")
elif playertotal2>playertotal1 and playertotal2<21:
        print(name2, "wins congrats!")
elif playertotal1>21 and playertotal2<21:
        print(name2, "wins congrats")
elif playertotal1<21 and playertotal2>21:
    print (name1,  "congrats")
elif playertotal1== playertotal2:
    print(name1 ,"and", name2, "draw")
print("thanks for playing", end = ' have a nice day')

