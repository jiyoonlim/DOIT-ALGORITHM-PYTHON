#  가로, 세로 길이가 정수이고
# 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('enter the area of rectangle: '))

for i in range(1, area+1):
  if i * i > area:
    break
  if area % 1:
    continue
  print(f'{i} x {area // i}')