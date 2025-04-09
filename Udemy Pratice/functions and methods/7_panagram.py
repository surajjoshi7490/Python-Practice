import string

def is_pangram(s):
    sentence=s.replace(" ","").lower()
    repeted_char=set(sentence)
    alphabet=set(string.ascii_lowercase)
    return alphabet.issubset(repeted_char)
print(is_pangram("The quick brown fox jumps over the lazy dog"))

