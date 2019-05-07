class Node():
    def __init__(self, dataIn):
        self.data = dataIn
        self.children = list()

    def add_children(self, nodeToAdd):
        self.children.append(nodeToAdd)

    def search(self, dataRequired):
        if self.data == dataRequired:
            return True  # data on Node
        for child in self.children:
            if child.search(dataRequired):
                return True  # data was on one of the children
        return False  # data not found


# initialisation
root = Node("this is the data")

# insertion
next_node = Node("Going to be next!")
root.add_children(next_node)

# search
root.search("Going to be next!")  # True
root.search("Not in the tree")  # False
