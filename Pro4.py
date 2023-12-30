#TASK - 4

import random

print("-----------ROCK-PAPER-SCISSORS-GAME-----------")

player_score = 0
system_score = 0
Tie = 0

name = input(" Enter the name Full Name : ")
print("Success Chances : \n 1. Rock vs Scissore == Rock\n 2. Paper vs Rock == Paper \n 3. Scissors vs Paper == Scissors")
print("\n")

while(1):
    
 print("Press\n 1. Paper\n 2. Rock \n 3. Scissor")
 print("\n")
 choice = int(input("Enter your choice : "))
 print("\n")

 while(choice>3):
   choice = int(input("Enter the valid input..!!!!"))



 if(choice == 1):
    player = "Paper"
 elif(choice==2):
    player = "Rock"
 else:
    player = "Scissors"

 print("The player's choice is ", player)
 
 print("Now System turn ")

 sys= random.randint(1,3)

 if(sys == 1):
    system = "Paper"
 elif(sys==2):
    system = "Rock"
 else:
    system = "Scissors"

 print("The System choice is ", system)


 if(system==player):
    print("TIE..!!!!!\n")
    score = "TIE"

 elif((system == "Paper" and player == "Scissors") or (system == "Scissors" and player == "Paper") ):
    print("Scissor Wins\n")
    score = "Scissor"

 elif((system == "Paper" and player == "Rock") or (system == "Rock" and player == "Paper")):
    print("Paper Wins\n")
    score= "Paper"

 else:
    print("Rock Wins\n")
    score = "Rock"


 if score == "TIE" :
    Tie+=1

 elif score == player:
    player_score+=1
 else:
    system_score+=1


 print(" Score Board Is : ")

 print(name," 's score is ",player_score)

 print("System's Score is ", system_score)

 print(" Total Ties are ", Tie)


 flag = int(input("Do you wnat to play again (1 = yes)/(0 = No) : "))


 if(flag == 0):
    break
 

if(player_score > system_score):
    print("The Game Winner is ", name)
    print("\n")
elif(system_score==player_score):
   print("Sorry no one is Winner of this Game..!!!")
   print("\n")
else:
   print("\nThe Game Winner is System")
   print("\n")


   print("Game Over\n")



