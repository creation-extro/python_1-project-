f =open("txtfile1.txt","r")
print(f.read(5))
"""for x in f:
    print(x)""" #u can use it for loop
f.close()
f=open("txtfile1.txt","a")
f.write("i have lots of money")
f=open("txtfile1.txt","r")
print(f.read())

f.close()