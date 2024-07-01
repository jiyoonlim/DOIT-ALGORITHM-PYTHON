# 오픈 주소법을 구현하는 해시 클래스 OpenHash 사용

from enum import Enum
from open_hash import OpenHash


Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료']) # 메뉴를 선언

def select_menu() -> Menu:
  """메뉴 선택"""
  s = [f'({m.value}){m.name} for m in Menu']
  while True:
    print(*s, sep=' ', end='')
    n = int(input(': '))
    if 1 <= n <= len(Menu):
      return Menu(n)

hash = OpenHash(13) #크기가 13인 해시 테이블을 생성

while True:
  menu = select_menu() # 메뉴 선택

  if menu == Menu.추가: # 추가
    key = int(input('추가할 키를 입력하세요: '))
    val = input('추가할 값을 입력하세요: ')
    if not hash.add(key, val):
      print('추가를 실패했습니다.')
  
  elif menu == Menu.삭제: 
    key = int(input('삭제할 키를 입력하세요: '))
    if not hash.remove(key):
      print('삭제를 실패했습니다')

  elif menu == Menu.검색:
    