#how to extract emails with the help of "foundall"
import re
input="""Hello from shubhamg199630@gmail.com
        to priya@yahoo.com about the meeting @2PM"""
emails=re.findall('\S+@\S+',input)
print(emails)