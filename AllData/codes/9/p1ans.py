lst = []
 
num = int(input())
 
lst = list(map(int, input().split()))
     
mn = 1000000000
for i in lst:
    if i%2==1:
        mn = min(mn,i)

print (mn)