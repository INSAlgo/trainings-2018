class Node():
    def __init__(self, char):
        self.charOnNode = char
        self.sucessor = list()
        self.nbNext = 0

    def store(self, chain, indice):
        self.nbNext += 1
        if indice == len(chain):
            return
        found = 0
        for s in self.sucessor:
            if s.charOnNode == chain[indice]:
                s.store(chain, indice + 1)
                found = 1
        if not found:
            nextNode = Node(chain[indice])
            self.sucessor.append(nextNode)
            nextNode.store(chain, indice + 1)

    def search(self, chain, indice):
        if indice == len(chain):
            return self.nbNext
        res = 0
        for s in self.sucessor:
            if s.charOnNode == chain[indice]:
                res += s.search(chain, indice + 1)
        return res


n = int(input())
root = Node("/")
for k in range(n):
    cmd = input().split()
    if cmd[0] == "add":
        root.store(cmd[1], 0)
    elif cmd[0] == "find":
        print(root.search(cmd[1], 0))
