# print * by n, but do line change every w

print('print *')
n = int(input('how do you want to print?: '))
w = int(input('몇 개 마다 줄바꿈 할까요?: '))

for i in range(n): #do n 
  print('*', end='')
  if i % w == w-1: # n번 판단
    print() #line change

if n % w:
  print()