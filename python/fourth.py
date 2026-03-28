#seaparate each digit of a number and print it on the new line.
num=int(input("Enter the number"))
while(num>0):
    print(num%10)
    num=num//10
#accept a number and print it reverse
num=int(input("Enter the number"))
rev=0
while(num>0):
    rev=rev*10+num%10
    num=num//10

print(rev)
while(rev>0):
    print(rev%10)
    rev=rev//10

#accept a number and check if it is a palindrome number
num=int(input("Enter the number:"))
copy=num
rev=0
while(num>0):
    rev=rev*10+num%10
    num=num//10
    
if(copy==rev):
    print(f"{copy}is a palindrone number")
else:
    print(f"{copy} is not a palindrome number")

#create a random number guessing game with python
import random
num=random.randint(1,11)
while True:
    guess=int(input("Enter the number-"))
    tries=+1
    if(guess==num):
        print(f"You are right {guess} and {num} match together at {tries}")
        break
    elif(guess>num):
        print(f"choose low at {tries}")
    elif(guess<num):
        print(f"go higher at {tries}")
    else:
        print(f"better next time buddy at {tries}")