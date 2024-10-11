a,b=input(),input()
idx = a.find(b)
ans=a
while(idx!=-1):
    ans = ans[:idx]+ans[idx+len(b):]
    idx = ans.find(b)
print(ans)