def greeting(name):
    print("Hello" + name )

import mymodule
mymodule.greeting("Tejaswi")

person={  
    "name" :"teju",
    
    "age" : 18,
    
    "country" :"india"
}
a = mymodule.person["age"]
print(a)
import mymodule as mx 
a1= mx.person["age"]
print(a)
import platform
x = platform.system()
print(x)
y=dir(platform)
print(x)

import datetime 

y = datetime.datetime.now()
print(y.year)
print(y.strftime("%A"))

import math 
w=math.sqrt(144)
print(w)

import re 

txt = "I live in india"
s= re.search("^I.*india$",txt)
if s:
    print("yes it is match")
else:
    print("it is not a match")
#to split the txt 
p= re.split("\s",txt)
print(p)

#TRY AND EXPECT 
"""try : lets you try the test of bock code of errors 
   expect: lets you handle the error 
   else : lets you excutes the code when there is no error"""
try:
    print(d)
except NameError:
    print("d is not defined  ")
except:
    print("samothing went wrong ")
else:
    print("nothing went wrong ")
finally:
    print("try expect is finished ") #This can be useful to close objects and clean up resources:
#i can also make a expection by using raise or throw 

