# 10 ~ 99 사이의 난수 n개 생성하기 (13이 나오면 중단)
import random

n = int(input("enter the number random's: "))

for _ in range(n):
 r = random.randint(10, 99)
 print(r, end=' ')
 if r == 13:
  print('\n stopping the program')
  break
else:
 print('\n stopping the program')