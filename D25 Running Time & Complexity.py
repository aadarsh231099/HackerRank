import math
n=int(input())
def isprime(num):
    if num<2:
        return False
    for i in range(2,int((math.sqrt(num)+1))):
        if num%i is 0:
            return False
        
    return True
for _ in range(n):
    num=int(input())
    if num>=2 and isprime(num):
        print("Prime")
    else:
        print("Not prime")