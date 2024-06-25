# print the maximum element of the sequcne

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
  """sequence a's maximum value return"""
  maximum=a[0]
  for i in range(1, len(a)):
    if a[i] > maximum:
      maximum = a[i]
  return maximum

if __name__ == '__main__':
  print('find the maximum element of an array')
  num = int(input("enter the number of elements: "))
  x = [None] * num

  for i in range(num):
    x[i] = int(input(f' x[{i}]값을 입력하세요: '))
  print(f'the maximum value is {max_of(x)}')