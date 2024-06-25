print('print *')
n = int(input('how many to print: '))
w = int(input("몇 개 마다 줄바꿈?: "))

for _ in range(n//w):
  print('*' * w)

rest = n % w
if rest:
  print('*' * rest)
        