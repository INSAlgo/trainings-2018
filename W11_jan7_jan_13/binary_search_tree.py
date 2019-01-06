class BinarySearchTree:
    """Binary search tree implementation for multisets
    """

    def __init__(self, value=None):
        """Initialize a binary search tree. Use the optional parameter value
           to create a root node or leave empty for an empty tree.
        """
        self.value = value    # None means the tree is empty
        self.left = None
        self.right = None

    def from_list(values):
        """Generate a binary search tree from a list of values
        """
        tree = BinarySearchTree()
        for value in values:
            tree.insert(value)
        return tree

    def search(self, value):
        """Search the value in the tree. Returns a boolean
        """
        if self.value is None:
            return False
        elif self.value == value:
            return True
        elif self.value > value:
            return (self.left is not None) and self.left.search(value)
        else:
            return (self.right is not None) and self.right.search(value)

    def insert(self, value):
        """Insert the value in the tree
        """
        if self.value is None:
            self.value = value
        elif self.value > value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def delete(self, value):
        """Remove one occurence of the value in the tree if it is found
        """
        if self.value is None:
            return None
        elif self.value == value:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                left_rightmost = self.left
                while left_rightmost.right is not None:
                    left_rightmost = left_rightmost.right
                self.value = left_rightmost.value
                self.left = self.left.delete(left_rightmost.value)
        elif self.value > value:
            if self.left is not None:
                self.left = self.left.delete(value)
        else:
            if self.right is not None:
                self.right = self.right.delete(value)
        return self

    def traversal(self):
        """In-place traversal of the tree (returns an increasing list)
        """
        if self.value is None:
            return []
        left_part = self.left.traversal() if self.left is not None else []
        right_part = self.right.traversal() if self.right is not None else []
        return left_part + [self.value] + right_part

    def draw(self):
        """Draws a visual representation of the tree
        """
        print("\n".join(self.get_repr()))

    def get_repr(self):
        """Representation used by the draw function
        """
        if self.value is None:
            return []
        if self.left is None:
            repr_left = []
        else:
            repr_left = self.left.get_repr()
        if self.right is None:
            repr_right = []
        else:
            repr_right = self.right.get_repr()

        width_left = len(repr_left[0]) if repr_left else 0
        width_right = len(repr_right[0]) if repr_right else 0

        if len(repr_left) < len(repr_right):
            repr_left += (
                [" " * width_left] * (len(repr_right) - len(repr_left)))
        elif len(repr_left) > len(repr_right):
            repr_right += (
                [" " * width_right] * (len(repr_left) - len(repr_right)))

        repr_self = [" " * width_left + str(self.value) + " " * width_right]
        ll = len(str(self.value))
        for i in range(len(repr_left)):
            repr_self.append(repr_left[i] + " " * ll + repr_right[i])

        return repr_self


bst = BinarySearchTree.from_list([8, 3, 10, 1, 6, 4, 7, 14, 13])
