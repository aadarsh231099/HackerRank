n=int(input())
d={}

for i in range(n):
    x=input().split()
    d[x[0]]=x[1]
while 1:
    try:
        nm=input()
        if nm in d:
            print(nm,"=",d[nm],sep="")
        else:
            print("Not found")
    except:
        break
