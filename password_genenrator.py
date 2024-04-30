import random

length = int(input("Enter the length of passwords: "))

numbers= [] 
for x in range(48,58): 
    x=chr(x)
    numbers.append(x)
lowercases = []
for x in range(97,123): 
    x=chr(x)
    lowercases.append(x)
uppercases = [] 
for x in range(65,91): 
    x=chr(x)
    uppercases.append(x)
symbols = [] 
for x in range(33,39): 
    x=chr(x)
    symbols.append(x)
x=64
x=chr(x)
symbols.append(x)
rand_number=random.choice(numbers)
rand_up=random.choice(uppercases)
rand_low=random.choice(lowercases)
rand_symbol=random.choice(symbols)
combine_list=numbers + lowercases + uppercases + symbols
password= rand_number + rand_up + rand_low + rand_symbol 
for x in range(length-4):
    a=random.choice(combine_list)
    password=password+a
print(password)