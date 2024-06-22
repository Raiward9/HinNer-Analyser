from __future__ import annotations
from dataclasses import dataclass

class Empty:
    pass

@dataclass
class Node:
    symbol: str
    children: list
    type: Tree

Tree = Node | Empty