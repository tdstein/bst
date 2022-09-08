from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List, SupportsInt, TypeAlias, Union, SupportsFloat

T: TypeAlias = Union[int, float]


def from_list(_: List[T], i: int = 0) -> Optional[Node]:
    if len(_) == 0:
        return None

    value = _[i]
    if value is None:
        return None

    li = 2 * i + 1
    ri = 2 * i + 2

    left = None
    if len(_) > li:
        left = from_list(_, li)

    right = None
    if len(_) > ri:
        right = from_list(_, ri)

    return Node(_[i], left, right)


def _validate(node: Optional[Node], minimum: float = float('-inf'), maximum: float = float('inf')) -> bool:

    if node is None:
        return True

    return minimum < node.value < maximum\
        and _validate(node.left, minimum, node.value)\
        and _validate(node.right, node.value, maximum)


@dataclass
class Node:
    value: T
    left: Optional[Node] = None
    right: Optional[Node] = None

    def validate(self) -> bool:
        return _validate(self)

    def maximum(self) -> T:
        node = self
        while True:
            if node.right is None:
                return node.value
            node = node.right

    def minimum(self) -> T:
        node = self
        while True:
            if node.left is None:
                return node.value
            node = node.left

    def contains(self, value: T) -> bool:
        node = self
        while True:
            if node is None:
                return False
            elif node.value == value:
                return True
            elif value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right

    def insert(self, value: T) -> Node:
        node = self
        while True:
            if node.value == value:
                return node
            elif value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return node.left
                elif node.left.value < value:
                    tmp = Node(value, left=node.left)
                    node.left = tmp
                    return tmp
                else:
                    node = node.left
            elif value > node.value:
                if node.right is None:
                    node.right = Node(value)
                    return node.right
                elif node.right.value > value:
                    tmp = Node(value, right=node.right)
                    node.right = tmp
                    return tmp
                else:
                    node = node.right

    def delete(self, value: T) -> bool:
        node = self
        while True:
            if node.value == value:
                raise RuntimeError("Cannot delete root.")
            elif value < node.value:
                if node.left is None:
                    return False
                elif node.left.value == value:
                    node.left = node.left.left
                    return True
                else:
                    node = node.left
            elif value > node.value:
                if node.right is None:
                    return False
                elif node.right.value == value:
                    node.right = node.right.right
                    return True
                else:
                    node = node.right
