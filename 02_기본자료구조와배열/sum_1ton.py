# sum from 1 to n

def sum_1ton(n):
  """1 to n sum"""
  s = 0
  while n > 0:
    s += n
    n -= 1
  return s

x = int(input('enter value of x: '))
print(f'1 to {x} sum is {sum_1ton(x)}')