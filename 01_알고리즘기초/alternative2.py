# print + and - alternative version 2

print('print + and - alternatively')
n = int(input("How many do you want to print?: "))

for _ in range(n // 2):
  print('+-', end='')

if n % 2:
  print('+', end='')

print()

