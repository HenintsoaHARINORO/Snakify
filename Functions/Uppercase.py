str = "danced"
words = str.split(' ')
final = []


def capitalize_letter(word):
    return word.replace(word[0], chr(ord(word[0]) - 32),1)


for word in words:
    final.append(capitalize_letter(word))

print(' '.join(final))
"""
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
"""

