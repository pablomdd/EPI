# Pythonic way
def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s) // 2))


# word = "anitalavalatina"
# word = "nosferartu"
word = "aoipioa"

print(is_palindromic(word))