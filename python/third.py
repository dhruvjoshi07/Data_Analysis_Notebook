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

