n = int(input())
stri=""

def rev(n):
    if n == 0:
        return 0
    else:
        return str(n)

while n != 0:
    n = int(input())
    print(rev(n))
    n = int(input())