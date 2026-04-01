# question 1:
num1=int(input("Enter the number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    print(f"number is {num1} greater than {num2}")
else:
    print(f"second number is {num2} greater than {num1}")

# question 2:
response=str(input("Enter the gender: ")).lower()
if response=="male":
    print("Good Morning Sir")
elif response=="female":
    print("Good morning mam")
else:
    print("Good morning")

# question 3:
num=int(input("Enter the number:"))
if num/2==0:
    print(f"The {num} is a even number")
else:
    print(f"The {num} is a odd number")

# question 4:
name=input("enter your name: ")
age=int(input("Enter your age: "))
if age==18:
    print(f"hello {name} you are a valid voter")
elif age>18:
    print(f"hello {name} you are a valid voter")
else:
    print(f"hello {name} you need to wait")

# question 5
year=int(input("Enter year"))
if year%100==0 and year%400==0:
    print(f"{year} is a leaf year")
elif year%4==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} not a leap year")

