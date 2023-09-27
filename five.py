#search
import re
input="full stack developer"
found=re.search("stack",input)

if found:
    print("match is found")
else:
    print("match is not found")
