import collections

# Time: O(n) -> Linear
# Space: O(c) -> Constant <- each disctinc character

# Long
def can_form_palindrome(s: str):
    letters = [l % 2 for l in collections.Counter(s).values()]
    print(letters)
    return sum(letters) <= 1

# Shorter

def can_form_palindrome_short(s: str):
    return sum(l % 2 for l in collections.Counter(s).values()) <= 1


word = "anitalavalanita"
# word = "aeirosdsasd"
# print(can_form_palindrome(word))
print(can_form_palindrome_short(word))