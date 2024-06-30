# 체인법을 구현하는 해시 클래스 ChainedHash 사용

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료']) # 메뉴를 선언

def select_menu() -> Menu:
  """메뉴 선택"""
  s = [f'({m.value}){m.name}' for m in Menu]