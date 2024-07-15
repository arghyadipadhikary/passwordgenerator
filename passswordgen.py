import string
import random
a=string.ascii_letters
b=string.digits
c=string.punctuation
e=a+b+c
list(e)
l=[]
user = int(input("enter length of password you want."))
for i in range(user):
    f = random.choice(e)
    l.append(f)
print("your password is:- ",end="")
for i in l:
    print(i,end="")