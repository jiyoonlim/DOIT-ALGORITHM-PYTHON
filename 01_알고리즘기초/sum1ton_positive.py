# 1 to n, find the sum of integers (n>0)

print('Find the sum of integers from 1 to n')

while True:
  n = int(input('enter n: '))
  if n > 0:
    break

sum = 0
i = 1

for i in range(1, n+1):
  sum += i
  i += 1

print(f'1 to {n} the sum is {sum}')