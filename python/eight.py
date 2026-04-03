# EXCEPTION HANDLING AND FILE HANDLING
x=str(input("Enter the name:"))
try:
    d1={
        1:"hello",
        "hello":1,
        2:34,
        "list":[2,3,4,1,2],
        (1,2,3):"tuple",
        "a":{1,},
        3:{1}
    }
except Exception as err:
    raise ValueError(f"error{err}")
permission=input("Do u want help in methods:yes/no").strip().lower()
if permission=="yes":
    help(dict)
print(f"Your name is {x} and dictionary is {d1}")
y={10:100,20:200,30:300,40:400}
z={40:400,50:500,60:600,20:200}
for i in z:
    if i in y.keys():
        y[i]+=z[i]
    else:
        y[i]=z[i]
d2=z
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d2)
for i in d2:
    d1[i]=d2[i]
print(d1)
r=open("sample.txt",'w')
r.write("This is file of file handling")
r.close()

