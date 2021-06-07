n=int(input())
for j in range(0,n): 
     a=''
     b=''  
     s=str(input())
     for i in range(0,len(s)):
         if(i%2==0):
             a=a+s[i]
         else:
             b=b+s[i]
     print(a+ " " +b)