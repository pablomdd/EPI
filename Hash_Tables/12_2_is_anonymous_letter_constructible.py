import collections 

def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str):
    char_frequency = collections.Counter(letter_text)

    for c in magazine:
        if c in char_frequency:
            char_frequency[c] -= 1
            if char_frequency[c] == 0:
                del char_frequency[c]
                if not char_frequency:
                    return True

    return not char_frequency

# magazine = "ffqwrrs"
magazine = "asadasdaffdqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"
# letter = "hola soy pablo" 
letter ="fffsaaswnkams"     

print(is_letter_constructible_from_magazine(letter, magazine))