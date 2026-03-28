# if-elif ladder
name=str(input("Hello there ! May I know Your Name :"))
temp=int(input(f"Good Morning {name} ! Now tell me what's temperature you are dealing with :"))
if temp <0:
    print(f"{name} its fucking Freezing Cold at {temp} degree celsius....")
elif temp>=0 and temp<10:
    print(f"{name} its very Cold at {temp} degree celsius....")
elif temp>=10 and temp<20:
    print(f"{name} its fucking Cold at {temp} degree celsius....")
elif temp>=20 and temp<30:
    print(f"{name} its fucking pleasant at {temp} degree celsius....")
elif temp>=30 and temp<40:
    print(f"{name} its fucking Hot at {temp} degree celsius....")
else:
    print(f"{name} its very hot at {temp} degree celsius....")
# repeatation
name=str(input("Enter your name : "))
n=int(input(f"{name}! Enter the times you want to print hello {name}! "))
for i in range(n):
    print(f"hello {name}")
# natural number
m=int(input(f"{name}! Enter the end of natural number: "))
for i in range(1,m+1):
    print(i)
#rev
a=int(input(f"{name}! Enter the number to reverse"))
for i in range(a,0,-1):
    print(i)
# table
num=int(input("Enter the number: "))
for i in range(num,num*10+1,num):
    print(f"{num}*{i//num}={i}")
#sum upto n terms
sum=0
for i in range(0,num+1):
    sum=sum+i

print(sum)
# factorial

# sum of all even and odd numbers in range seaprately
num = int(input("Enter the number: "))

even_sum = 0
odd_sum = 0

for i in range(1, num+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

