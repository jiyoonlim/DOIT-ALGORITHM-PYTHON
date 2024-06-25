from max import max_of
print('find the maximum value from array')
print('caution: typing "End" will terminate the program')

number = 0
x = []

while True:
  s = input(f'x[{number}]값을 입력하세요: ')
  if s == 'End':
    break
  x.append(int(s)) # add to the end of array
  number += 1

print(f'{number}개를 입력했습니다.')
print(f'최댓값은 {max_of(x)} 입니다')
