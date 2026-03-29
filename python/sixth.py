# # <-------------LIST CONCEPT------------------>
# list=[10,21,11,78,56]
# list.append(43)
# list.insert(3,22)
# print(list)

# for i in list:
#     print(i)

# for i in range(len(list)):
#     print(list[i])

# # to find all methods of list
# print(dir(list))

# # to know methods what to do
# help(list)

# l=[3,2,-1,6,-7,8]
# l.append(-4)
# l.insert(2,9)

# # print positive and negative elements of an list
# print(f"the postive number is-")
# for i in l:
#     if i>0:
#         print(i)

# print("The negative numbers are-")
# for i in l:
#     if i<0:
#         print(i)

# # mean of list elements
# sum=0
# for i in l:
#     sum=+i

# print(sum/len(l))

# # find the greatest element and print its index too
# li=[3,6,2,1,8,0,4,7,12]
# greatest=li[0]
# index=0
# for i in range(len(li)):
#     if greatest<li[i]:
#         greatest=li[i]
#         index=i
# print(f"your largest number is {greatest} at index {index}")

# find the second greatest element
lt=[4,3,8,1,9,4]
greatest=lt[0]
sec_greatest=lt[0]
for i in range(len(lt)):
    if lt[i]>greatest:
        sec_greatest=greatest
        greatest=lt[i]
    elif lt[i] >sec_greatest:
        sec_greatest=lt[i]
    
print(f"The greatest is: {greatest} and second greatest is: {sec_greatest}")
# check if list is sorted or not