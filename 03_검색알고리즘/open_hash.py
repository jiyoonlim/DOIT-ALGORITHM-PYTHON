# 오픈 주소법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
  OCCUPIED = 0 # 데이터를 저장
  EMPTY = 1 # 비어 있음
  DELETED = 2 # 삭제 완료

class Bucket:
  """해시를 구성하는 버킷"""
  def __init__(self, key:Any = None, value:Any = None,
               stat: Status = Status.EMPTY) -> None:
    """초기화"""
    self.key = key
    self.value = value
    self.stat = stat
  
  def set(self, key:Any, value:Any, stat:Status) -> None:
    """모든 필드에 값을 설정"""
    self.key = key
    self.value = value
    self.stat = stat

  def set_status(self, stat:Status) -> None:
    """속성을 설정"""
    self.stat = stat

class OpenHash:
  """오픈 주소법으로 구현하는 해시 클래스"""
  def __init__(self, capacity: int) -> None:
    """초기화"""
    self.capacity = capacity # 해시 테이블의 크기를 지정
    self.table = [Bucket{}] * self.capacity # 해시 테이블

  def hash_value(self, key:Any) -> int:
    """해시값을 구현"""
    if isinstance(key, int):
      return key % self.capacity
    return(int(hashlib.md5(str(key).encode()).hexdigest(), 16) % self.capacity)
  
  def rehash_value(self, key:Any) -> int:
    """재해시값을 구함"""
    return(self.hash_value(key) + 1) % self.capacity
  
  def search_node(self, key:Any) -> Any:
    """키가 key인 버킷을 검색"""
    hash = self.hash_value(key) #검색하는 키의 해시값
    p = self.table[hash] # 버킷을 주목

    for i in range(self.capacity):
      if p.stat == Status.EMPTY:
        break
      elif p.stat == Status.OCCUPIED and p.key == key:
        return p
      hash = self.rehash_value(hash) #재해시
      p = self.table[hash]
    return None
  
  
