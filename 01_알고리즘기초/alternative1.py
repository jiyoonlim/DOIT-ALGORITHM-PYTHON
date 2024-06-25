# alternatively print + and -

print("print + and - alternatively")
n = int(input('how many to print?: '))

for i in range(n):
  if i % 2: # 1 is true
    print('-', end='') # print if odd
  else: # 0 is false
    print('+', end='') # print if even

print()