from __future__ import annotations
from dataclasses import dataclass
from typing import Any
from collections import deque

import yaml


@dataclass
class Node:
    key: Any
    data: Any = None
    left: Node = None
    right: Node = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Node = None

    def empty(self) -> bool:
        return self.root is None

    def zigzag_level_order_traversal(self) -> list[list[Any]]:
        res =[]
        q = deque([self.root] if self.root else [])
        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.key)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level = level[::-1] if len(res) % 2 else level
            res.append(level)
        return list(res)

def build_tree(list_view: list[Any]) -> BinaryTree:
    bt = BinaryTree()
    nodes = []
    for e in list_view:
        node = Node(e) if e is not (None) else None
        nodes.append(node)

    for i, node in enumerate(nodes):
        if node is None:
            continue
        if 2 * i + 1 < len(list_view): node.left = nodes[2 * i + 1]
        if 2 * i + 2 < len(list_view): node.right = nodes[2 * i + 2]

    if len(nodes) != 0: bt.root = nodes[0]
    return bt



if __name__ == "__main__":
    # Let's solve Binary Tree Zigzag Level Order Traversal problem from leetcode.com:
    # https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    # First, implement build_tree() to read a tree from a list format to our class
    # Second, implement BinaryTree.zigzag_traversal() returning the list required by the task
    # Avoid recursive traversal!

    with open(
        "practicum_6homeworkbinary_tree_zigzag_level_order_traversal_cases.yaml", "r"
    ) as f:
        cases = yaml.safe_load(f)

    for i, c in enumerate(cases):
        bt = build_tree(c["input"])
        zz_traversal = bt.zigzag_level_order_traversal()
        print(f"Case #{i + 1}: {zz_traversal == c['output']}")

