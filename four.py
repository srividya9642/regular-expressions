#match()
import re
input="full stack python"
found=re.match("stack",input)
if found:
    print("match is found")
else:
    print("match is not found")