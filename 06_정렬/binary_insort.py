# 이진 삽입 정렬 알고리즘 구현 using "binary insort"

from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
  for i in range(1, len(a)):
    bisect.insort(a, a.pop(), 0, i)
