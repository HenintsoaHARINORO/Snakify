numbers = list(map(int, input().split()))
n_alice = numbers[0]
n_bob = numbers[1]
set_alice = set()
set_bob = set()
for _ in range(n_alice):
    set_alice.add(int(input()))
print(set_alice)
for _ in range(n_bob):
    set_bob.add(int(input()))
print(set_bob)
set1 = set_alice.intersection(set_bob)
set2 = set_alice.difference(set_bob)
set3 = set_bob.difference(set_alice)
print(len(set1))
for num in sorted(set1):
    print(num, end="")
    print()
print(len(set2))

for num in sorted(set2):
    print(num, end="")
    print()
print(len(set3))
for num in sorted(set3):
    print(num, end="")
    print()

"""
def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])

N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))

print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)
"""