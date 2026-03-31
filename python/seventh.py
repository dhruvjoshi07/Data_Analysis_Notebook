#write a py script to merege 2 py dictionaries
a={
    1:"hello",
    "a":23,
    3:{2,3,1,4,4,2},
    4:[32,44,12,56,33],
    5:{1,2,3,4,5}
}
b={
    6:3.12,
    7:{1},
    8:{2,},
    9:"D+3"
}
a.update(b)
print(a)

for i in b:
    a[i]=b[i]
    print(a)

#write a py program to sum all the values in a dictionary
sum=0
for i in a:
    sum=sum + a[i]

print(sum)

#count the frequency of each elements in a list
a=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)

#write a python program to combine 2 dictionary by adding values for common keys
d1={10:100,20:200,40:400}
d2={40:400,50:500,60:600}
for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]