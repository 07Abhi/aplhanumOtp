from threading import*
import random as rd
from time import sleep
s=""
d=""
class demo:
    def word(self):
        global s
        
        
        for i in range(0,3):
            k=rd.randint(48,57)
            o=chr(k)
            s=s+o
            print(o)
            sleep(1)
            
    
    def num(self):
        global d
        for k in range(0,3):
            u=rd.randint(10,127)
            y=chr(u)
            d=d+y
            print(y)
            sleep(1)
obj=demo()
t1=Thread(target=obj.word)
t2=Thread(target=obj.num)

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
r=s+d
print("OTP=",r)
    
