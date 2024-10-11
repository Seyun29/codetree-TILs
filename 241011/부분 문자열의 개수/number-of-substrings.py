import re

a,b=input(),input()
cnt=0
for idx, w in enumerate(a):
    if a[idx:idx+len(b)]==b:
        cnt+=1
print(cnt)