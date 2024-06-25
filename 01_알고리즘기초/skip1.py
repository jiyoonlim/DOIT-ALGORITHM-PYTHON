# 1 ~ 12 print but skip 8

for i in range(1, 13):
  if i == 8:
    continue
  print(i, end=', ')

print()