actions= {
  'read': 'R',
  'write': 'W',
  'execute': 'X',
}
n = int(input())
file_rights = {}
d1 ={}
l1=[]
for i in range(n):
    l1 = input().split(' ')
    d1[l1[0]]= l1[1:]
print(l1)
print(d1)

n2= int(input())

for _ in range(n2):
  action, filename = input().split()
  if actions[action] in d1[filename]:
    print('OK')
  else:
    print('Access denied')
"""
OPERATION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    operation, file = input().split()
    if OPERATION_PERMISSION[operation] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')
"""

