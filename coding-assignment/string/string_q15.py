#Rearrange Words in a Sentence
def reverseWords(s: str) -> str:
    words = s.split()
    return ' '.join(reversed(words))
