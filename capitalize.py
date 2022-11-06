def solve(s):

    if " " in s:
        s = s.split(" ")
    else:
        s = [s]
    new = []
    for word in s:
        try:
            if word[0].isalpha():
                new.append(f"{word[0].upper()}" + f"{word[1:]}")
            else:

                new.append(word)
        except IndexError:
            new.append(word)
    return " ".join(new)


# print(solve("1212aa"))
# print(solve("a a a"))
print(
    solve(
        "q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M"
    )
)
