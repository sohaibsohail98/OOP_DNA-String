scrabble_score = {"a": 1, "b": 3, "c": 3, "d": 2,
                 "e": 1, "f": 4, "g": 2, "h": 4,
                 "i": 1, "j": 8, "k": 5, "l": 1,
                 "m": 3, "n": 1, "o": 1, "p": 3,
                 "q": 10, "r": 1, "s": 1, "t": 1,
                 "u": 1, "v": 4, "w": 4, "x": 8,
                 "y": 4, "z": 10}

# Creates a function which takes 1 argument
def scrabble_game(word):

    score = 0
    for n in word:
        n = n.lower()
        score = score + scrabble_score[n]
    return score

enter_letter = input("Word score: ")

print(scrabble_game(enter_letter))
