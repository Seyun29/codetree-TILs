import re

a = input()
print(sum(list(map(int,list(re.findall(r'\d+',a))))))