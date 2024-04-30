def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a+b
def div(a,b):
    return a-b

a=int(input("enter first number \n"))
b=int(input("enter second number \n"))

choice=input("ENTER ADD TO ADD THE NUMBER \n SUBTRACT TO SUBTRACT THE NUMBER \n MULTIPLE TO MULTIPLE THE NUMBER \n DIVIDE TO DIVIDE THE NUMBER \n")
if choice=="ADD" or choice=="Add" or choice=="add" or choice=="+" or choice=="1":
    sum=add(a,b)
    print(sum)
elif choice=="SUBTRACT" or choice=="Subtract" or choice=="subtract" or choice=="-" or choice=="2":
    subtraction=sub(a,b)
    print(subtraction)
elif choice=="MULTIPLE" or choice=="Multiple" or choice=="multiple" or choice=="*" or choice=="3":
    multipication=multi(a,b)
    print(multipication)
elif choice=="DIVIDE" or choice=="Divide" or choice=="divide" or choice=="/" or choice=="4":
    division=div(a,b)
    print(division)
else:
    print("INVALID INPUT")
