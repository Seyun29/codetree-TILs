import re

a = input()
a = re.sub(r'[^a-zA-Z0-9]','',a).lower()
print(a)