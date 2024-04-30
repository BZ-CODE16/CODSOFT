import random

def rules(user,computer):
    if user==computer:
        return 0
    elif (user==3 and computer==4) or (user==4 and computer==2) or (user==2 and computer==3):
        return -1
    else:
        return 1
    
def input_user(i):
    if i=="scissor" or i=="Scissor" or i=="SCISSOR" or i=="S" or i=="s" or i=="2":
        return 2
    elif i=="rock" or i=="ROCK" or i=="Rock" or i=="R" or i=="r" or i=="0":
        return 3
    elif i=="PAPER" or i=="Paper" or i=="paper" or i=="P" or i=="p" or i=="5":
        return 4
    else :
        print("wrong input!!!")
def result(ans):
    if ans==-1:
        print("you loss!!!") 
    elif ans==0:
        print("tie!!!")         
    else:
       print("you win!!!")  
round=0      
while(round==0):
    user=input("enter rock paper or scissor:  ")
    turn_user=input_user(user)
    turn_computer=random.randint(2,4)
    r=rules(turn_user,turn_computer)
    result(r)
    round=int(input("enter 0 to entry:  "))
