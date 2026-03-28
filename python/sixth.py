# <-------------LIST CONCEPT------------------>
list=[10,21,11,78,56]
list.append(43)
list.insert(3,22)
print(list)

for i in list:
    print(i)

for i in range(len(list)):
    print(list[i])

# to find all methods of list
print(dir(list))

# to know methods what to do
help(list)

l=[3,2,-1,6,-7,8]
l.append(-4)
l.insert(2,9)

# print positive and negative elements of an list
print(f"the postive number is-")
for i in l:
    if i>0:
        print(i)

print("The negative numbers are-")
for i in l:
    if i<0:
        print(i)

# mean of list elements
sum=0
for i in l:
    sum=+i

print(sum/len(l))