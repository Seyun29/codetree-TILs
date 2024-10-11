a,b=input(),input()
ans=a
l,r=b.count('L'),b.count('R')
if(l>r):
    for i in range(l-r):
        ans=ans[1:]+ans[0]
elif(r>l):
    for i in range(l-r):
        ans=ans[-1]+ans[:-1]

print(ans)