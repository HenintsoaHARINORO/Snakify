n = int(input())
real_set = set()
i =1
while i <= n:
    real_set.add(i)
    i +=1
ans =set()

final = set()
while 'HELP' not in ans:
    print("not yet")
    ans.add(input())
    if 'YES' or 'NO' in ans:
        ans.discard('YES')
        ans.discard('NO')

else:
    ans.discard('HELP')
    print('HELP')

print(ans)
print(real_set)



