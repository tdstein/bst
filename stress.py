import random
from typing import Optional

from bst import Node

for i in range(1, 5):
    print(f"Running iteration {i}.")
    n = 10 ** i
    maximum = 10 ** (i + 1)
    vs = [random.randint(-maximum, maximum) for _ in range(n)]
    print(vs[:10])
    root = vs[0]
    bst = Node(root)
    vs = vs[1:]
    [bst.insert(v) for v in vs]
    print(root, bst.minimum(), bst.maximum())
    bst.validate()
    random.shuffle(vs)
    [bst.delete(v) for v in vs]
    assert bst == Node(root)
