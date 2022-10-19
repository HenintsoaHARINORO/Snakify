s = " "
n = " "
while n != '0':
    n = input()
    s = s + ' ' + n


def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

for num in reverse(s):
    print(num,end="")
    print()

"""
def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

reverse()
"""