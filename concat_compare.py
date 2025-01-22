import time
start1=time.time()
result1=""
for i in range (1,100001):
    result1+=str(i)
print(result1)
print("+= Time:", time.time()-start1)

start2=time.time()
result2="".join(str(i) for i in range (1-100001))
print(result2)
print("join() Time:", time.time()-start2)





