n = int(input())
result = set()

i = 1
while i <= n:
    result.add(str(i))
    i += 1
line = input()
while line != 'HELP':

    guess = set(line.split(' '))
    operation = input()
    if operation == 'YES':
        result = result.intersection(guess)  # maybe we need two sets
    elif operation == 'NO':
        result = result.difference(guess)
    line = input()
else:
    print(*(sorted(list(result))))
"""
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))
"""