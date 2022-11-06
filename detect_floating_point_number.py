import re


def is_float(number):
    letters = re.search("[a-zA-Z]", number)
    signs_inside = re.search(r"[+|-]+", number[1:])
    zero = re.search(r"0\d+\.", number)
    if letters or signs_inside or number.count(".") != 1 or zero:
        print("False")
    elif re.search("\d*\.\d+", number):
        print("True")
        a = 1
    else:
        print("False")


print(is_float("1-1.00"))
print(is_float("-+4.5"))  # f
print(is_float("4.0O0"))  # f
print(is_float("4.000"))  # t
print(is_float("-1.00"))  # t
print(is_float(".5"))  # t
print(is_float("-.7"))  # t
print(is_float("+.4"))  # t
print(is_float("-+4.5"))
print(is_float("12."))
print(is_float("12.0"))
print(is_float("12.1.1"))
