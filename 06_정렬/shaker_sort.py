# shaker sort

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
  """shaekr sort"""
  left = 0
  right = len(a) - 1
  last = right
  while left < right:
    for j in range(right, left, -1):
      if a[j-1] > a[j]:
        a[j-1], 