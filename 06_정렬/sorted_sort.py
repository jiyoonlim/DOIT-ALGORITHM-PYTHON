# sort using sorted() function

print('sorted() 함수를 사용하여 정렬합니다')
num = int(input('enter number of elements: '))
x = [None] * num

for i in range(num):
  x[i] = int(input(f'x[{i}]: '))

# 배열 x를 오름차순으로 정렬
x = sorted(x)
print('sorted using ascending')

