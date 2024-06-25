# 2자리 양수 (10~99) 까지 입력받기

print('enter a two digit positive integer: ')

while True:
  no = int(input('enter the value: '))
  if no >= 10 and no <= 99:
    break

print(f'the entered value is {no}')