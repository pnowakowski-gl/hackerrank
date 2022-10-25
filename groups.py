import re
a = '12345678910111213141516171820212223'
b = '..13AAaaa'
c = '12asdfgert'
list_ = [a, b, c]
for i in list_:
    match = re.search(r"([A-Za-z0-9])\1", i)
    if match:
        print(match.group(1))
    else:
        print(-1)