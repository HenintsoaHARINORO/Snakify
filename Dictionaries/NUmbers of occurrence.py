s_input = input()
words = {}
counts = []
for word in s_input.split():
    if word not in words:
        words[word] = 0
    else:
        words[word] += 1
    counts.append(words[word])

print(counts)
for element in counts:
    print(element, end=" ")

"""
counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
"""