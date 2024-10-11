strs = list()
for i in range(3):
    strs.append(input())

strs.sort(key=lambda x:len(x))
print(len(strs[-1])-len(strs[0]))