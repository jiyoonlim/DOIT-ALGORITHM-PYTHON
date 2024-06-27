# 커서를 이용한 연결 리스트 클래스 ArrayLinkedList 사용하기

from enum import Enum
from array_list import ArrayLinkedList

Menu = Enum('Menu', [ '머리에노드삽입', '꼬리에노드삽입', '머리노드삭제',
                     '꼬리노드삭제', '주목노드출력', '주목노드이동',
                     '주목노드삭제', '모든노드삭제', '검색', '멤버십판단',
                     '모든노드출력', '스캔', '종료'])