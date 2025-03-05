import math
import time
start=time.time()

def res(n):
    dp=[0]*10000
    for i in range(1,10000):
        for j in range(2*i,10000,i):
            dp[j]+=i
    count=0        
    for i in range(10000):
        j=dp[i]
        if j<10000 and dp[j]==i and i!=j:
            print(i)
            count+=j
    print(count)

res(5)
stop=time.time()
print(stop-start)
