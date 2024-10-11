a,b=input(),input()
ans=a
for d in b:
    if d=="L":
        ans=ans[1:]+ans[0]
    else:
        ans=ans[-1]+ans[:-1]

print(ans)