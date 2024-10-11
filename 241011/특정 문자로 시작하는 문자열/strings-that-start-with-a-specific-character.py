import math

n=int(input())
l = list()
for i in range(n):
    l.append(input())
key = input()

ans = list()
for w in l:
    if w.startswith(key):
        ans.append(w)
ans = list(map(lambda x:len(x), ans))
print(len(ans),f"{round(sum(ans)/len(ans),2):.2f}")