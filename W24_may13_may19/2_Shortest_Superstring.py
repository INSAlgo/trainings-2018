########################################
# Application of the Held Karp algorithm
########################################
from collections import deque
from collections import defaultdict


class Solution:

    def extract_bit(self, bitmap, rank):
        return (bitmap >> rank) % 2

    def put_bit(self, bitmap, rank, value):
        if value == 1:
            return bitmap | (1 << rank)
        else:
            return bitmap & ~(1 << rank)

    def Held_Karp(self, graph, nodeStart):
        # for a static structure :
        # mem = [[float('inf') for j in range(pow(2, len(graph)+1))]
        #       for i in range(len(graph))]
        # store distance:predecessor
        mem = defaultdict(lambda: defaultdict(lambda: [float('inf'), -1]))
        mem[nodeStart][pow(2, nodeStart)] = [0, -1]
        file = deque()
        file.append((nodeStart, 1 << nodeStart))
        while(file):
            nodeCurrent, setCurrent = file.popleft()
            # generate all neighbours of the current node :
            for neighbor in graph[nodeCurrent]:
                # discard neighbors already seen
                if not self.extract_bit(setCurrent, neighbor):
                    newBitmap = self.put_bit(setCurrent, neighbor, 1)
                    # never seen before
                    if mem[neighbor][newBitmap][0] == float('inf'):
                        file.append((neighbor, newBitmap))
                    # update the distance
                    if(mem[neighbor][newBitmap][0] > mem[nodeCurrent][setCurrent][0]
                            + graph[nodeCurrent][neighbor]):
                        mem[neighbor][newBitmap] = [mem[nodeCurrent][setCurrent]
                                                    [0]+graph[nodeCurrent][neighbor], nodeCurrent]
        bestDistance = float('inf')
        bestEnd = -1
        # find the best option with the return
        for node in range(len(graph)):
            if mem[node][(1 << len(graph))-1][0] < bestDistance:
                bestEnd = node
                bestDistance = mem[node][(1 << len(graph))-1][0]
        # reconstruct the path

        res = list()
        currBitMap = (1 << len(graph))-1
        while bestEnd != -1:  # go back to the precedent of every string used
            res.append(bestEnd)
            pre = mem[bestEnd][currBitMap][1]
            currBitMap = self.put_bit(currBitMap, bestEnd, 0)
            bestEnd = pre
        return res

    def numberCommon(self, s1, s2):
        common = 0
        for k in reversed(range(min(len(s1), len(s2)))):
            if(s1[len(s1)-k:] == s2[:k]):
                return k

    def shortestSuperstring(self, A: List[str]) -> str:
        graph = [{} for k in range(len(A)+1)]
        A = ["/"]+A
        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    graph[i][j] = len(A[j])-self.numberCommon(A[i], A[j])
        bestSequence = self.Held_Karp(graph, 0)[::-1]
        superstring = ""
        for k in range(1, len(bestSequence)):
            superstring += A[bestSequence[k]
                             ][len(A[bestSequence[k]])-graph[bestSequence[k-1]][bestSequence[k]]:]
        return superstring
