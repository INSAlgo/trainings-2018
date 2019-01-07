def traversal(root):
    part_left = traversal(root.left) if root.left is not None else []
    part_right = traversal(root.right) if root.right is not None else []
    return [str(root.info)] + part_left + part_right


def preOrder(root):
    print(" ".join(traversal(root)))
