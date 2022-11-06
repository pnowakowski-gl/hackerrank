import re

str1 = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
str2 = "bII1io2-aaa+aaab"
str3 = "abaabaabaabaaefEAEOUOIouf"
consonats = "QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm"

str_ = str2
found = re.finditer(r"([aeiouAEIOU]{2,})", str_)
matches = 0
if found:
    for f in found:
        start = f.span()[0] - 1
        end = f.span()[1]
        try:
            if str_[start] in consonats and str_[end] in consonats:
                print(f.group(0))
                matches += 1
        except IndexError:
            continue
else:
    print(-1)
if not matches:
    print(-1)
