class Solution(object):
    def letterCasePermutation(self, S):
        l1 = [""]
        for k in range(len(S)):
            l2 = []
            if(S[k].isalpha()):
                for e in l1:
                    l2.append(e + S[k].lower())
                    l2.append(e + S[k].upper())
                l1 = l2
            else:
                for i in range(len(l1)):
                    l1[i] += S[k]
        return l1
