#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)
a = [1,3,5,6]
x = 0
for i in a:
    if i>4: continue 
    x += i 
    print (x)