class Node():
    def __init__(self, char):
        self.charOnNode = char
        self.sucessor = list()
        self.endNode = 0

    def store(self, chain, indice):
        if self.endNode:  # if that node is already a leaf for another string
            return False
        if indice == len(chain):
            self.endNode = 1
            if len(self.sucessor) != 0:
                # The current string is a substring of another one
                return False
            return True

        found = 0
        res = True
        for s in self.sucessor:
            if s.charOnNode == chain[indice]:
                res = s.store(chain, indice + 1)
                found = 1
        if not found:
            nextNode = Node(chain[indice])
            self.sucessor.append(nextNode)
            nextNode.store(chain, indice + 1)
        return res


n = int(input())
root = Node("/")
for k in range(n):
    s = input()
    if not(root.store(s, 0)):
        print("BAD SET")
        print(s)
        break
else:
    print("GOOD SET")
