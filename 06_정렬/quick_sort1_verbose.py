from typing import MutableSequence
def qsort(a: MutableSequence, left:int, right:int) -> None:
  """a[left] ~ a[right]을 퀵 정렬 (배열을 나누는 과정 출력)"""
  pl = left
  pr = right
  x = a[(left + right) // 2] # pivot (middle element)

  print(f'a[{left}] ~ a[{right}]: ', *a[left: right+1]) # 새로 추가된 부분

  while pl <= pr:
    while a[pl] < x: pl += 1
    while a[pr] > x: pr -= 1
    if pl <= pr:
      a[pl], a[pr] = a[pr], a[pl]
      pl += 1
      pr -= 1

  if left < pr:
    qsort(a, left, pr)
  if pl < right:
    qsort(a, pl, right)
