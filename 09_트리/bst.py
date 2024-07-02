# 이진 검색 트리 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
  """이진 검색 트리의 노드"""
  def __init__(self, key:Any, value:Any, left:Node = None,
               right: Node = None):
    