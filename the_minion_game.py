def minion_game(string):
    players = {"Kevin": 0, "Stuart": 0}
    vowels = ["A", "E", "I", "O", "U"]
    string_length = len(string)
    for i in range(string_length):
        if string[i] in vowels:
            players["Kevin"] += string_length - i
        else:
            players["Stuart"] += string_length - i
    if players["Kevin"] == players["Stuart"]:
        return "Draw"
    return (
        f"{max(players, key=players.get)}"
        + f" {players[max(players, key=players.get)]}"
    )


print(minion_game("BANANA"))
print(minion_game("BANAASA"))
