import itertools as it
class Solution(object):
    def getPermutation(self, n, k):
        cpt = 0
        l = []
        for l in it.permutations(list(range(1,n+1)),n):
            if(cpt == k-1):
                return "".join(map(str,l))
            cpt+=1