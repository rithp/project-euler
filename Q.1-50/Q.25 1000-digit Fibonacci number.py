import math
import time
start=time.time()
a=1
b=1
count=1
while len(str(a)) <1000:
    a, b = b, a + b  
    count += 1
print(count)    

stop=time.time()
print(stop-start)
