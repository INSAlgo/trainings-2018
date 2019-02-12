from collections import deque, defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if root is None:
            return []
        dq = deque([(root, 0)])
        levels = defaultdict(list)
        levels[0].append(root.val)
        while dq:
            node, lvl = dq.popleft()
            for child in node.children:
                levels[lvl + 1].append(child.val)
                dq.append((child, lvl + 1))
        return [li for lvl, li in sorted(levels.items(), key=lambda x: x[0])]
