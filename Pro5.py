
#TASK - 5

import random


char = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()?|+[]"

while(1):
    length = int(input("\nEnter the length of the Password : "))

    password = ""

    for i in range(length):
       password+=random.choice(char)

    print("The Strongest Password is : ")
    print("\n",password,"\n")
     
    flag = int(input("Do you want to Generate The Password again : "))

    if(flag==0):
        break;
