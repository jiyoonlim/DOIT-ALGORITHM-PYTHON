# while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
  """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while문)"""
  i = 0

  while True: 
    if i == len(a):
      return -1           # 검색에 실패하여 -1를 반환
    if a[i] == key:
      return i            # 검색에 성공하여 현재 검사한 배열의 인덱스를 반환
    i += 1


if __name__ == '__main__':
  num = int(input('원소 수를 입력하세요: '))    # num값을 입력받음
  x = [None] * num                         # 원소 수가 num 인 배열을 생성

  for i in range(num):
    x[i] = int(input(f'x[{i}]: '))

  ky = int(input('검색할 값을 입력하세요: '))   # 검색할 키를 입력받음

  idx = seq_search(x,ky)                  # 키와 값이 같은 원소를 x에서 검색

  if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
  else:
    print(f'검색값은 x[{idx}] 에 있습니다. ')


