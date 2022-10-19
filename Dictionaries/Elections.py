n = int(input())
list1 = []
list2 = []
list3 = []
list4 = []
dict = {}
for i in range(n):
    list1.append(input().split(' '))

for i in range(len(list1)):
    list2.append(list1[i][0])
    list3.append(list1[i][1])

for el in list3:
    list4.append(int(el))

i = 0
while i < len(list2):
    for el in list2:
        if el in dict:
            dict[el] += list4[i]

        else:
            dict[el] = list4[i]

        i += 1
for key, value in sorted(dict.items()):
    print(key, dict[key])
"""
num_votes = {}
for _ in range(int(input())):
    candidate, votes = input().split()
    num_votes[candidate] = num_votes.get(candidate, 0) + int(votes)

for candidate, votes in sorted(num_votes.items()):
    print(candidate, votes)
"""