a,b = input(),input()

cnt=0
s=a
ans=-1
while cnt<=len(a):
    cnt+=1
    s=s[-1] + s[:-1]
    if (s==b):
        ans=cnt
        break

print(ans)