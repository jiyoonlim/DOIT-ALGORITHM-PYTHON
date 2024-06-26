# 리스트에서 임의의 원소값 업데이트하기
def change(lst, idx, val):
  """lst[idx]의 값을 val로 업데이트"""
  lst[idx] = val

x = [11,22,33,44,55]
print('x = ', x)

index = int(input('pick an index to update: '))
value = int(input('enter the new value: '))

change(x, index, value)
print(f'x = {x}')