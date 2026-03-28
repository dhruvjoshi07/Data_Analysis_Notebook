def palindrome(st):
    copy=st
    rev=0
    while st>0:
        rev=rev*10+st%10
        st=st//10
    if(rev==copy):
        print("is a palindrome")
    else:
        print("not a palindrome")

a=int(input("Enter the string-"))
palindrome(a)

b=3213166878769781269
palindrome(b)

def hello():
    return "abc"
print(hello())