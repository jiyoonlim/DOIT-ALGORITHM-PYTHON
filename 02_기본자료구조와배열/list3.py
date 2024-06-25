# 리스트의 모든 원소를 enumerate() 함수로 스캔하기 (1부터 카운터))

x = ['a', 'b', 'c', 'd']

for i, name in enumerate(x,1):
  print(f'{i} 번째 = {name}')


for i, name in enumerate(x):
  print(f'{i} 번째 = {name}')