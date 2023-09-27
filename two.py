import re
input=''' full stack python
java fulln stack
mern stack'''
found=re.match(r"full",input)
print(found)
if found:
    print("match found")
else:
    print("match not found")
