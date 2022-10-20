
d1 = {}
n =int(input())
words =[]
words1= []
for _ in range(n):
    words.append(input().split(' '))
print(words)
for rows in words:
  for columns in rows:
    words1.append(columns)
print(words1)
for element in words1:
    if element in d1:
        d1[element] +=1
    else:
        d1[element]=1
print(d1)

for i in sorted(set(d1.values()), reverse=True):
  for word in sorted([word for word in d1 if d1[word] == i]):
    print(word)
"""
from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

# You can also solve this problem without Counter:
#
# n = int(input())
# counts = {}
# for _ in range(n):
#     for word in input().split():
#         counts[word] = counts.get(word, 0) + 1
#
# freqs = [(-count, word) for (word, count) in counts.items()]
# for c, word in sorted(freqs):
#     print(word)
"""