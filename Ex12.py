

def toggle(phrase):
    new_phrase = ""
    for letter in phrase:
        if letter in ['a', 'e', 'i', 'o', 'u'] or letter in ['A', 'E', 'I', 'O', 'U']:
            new_phrase += letter.lower()
        else:
            new_phrase += letter.upper()
    return new_phrase


print(toggle(input("Enter a phrase: ")))