import re
input="full stack python"
found=re.match("full",input)
if found:
    print("match is found")
else:
    print("match is not found")
