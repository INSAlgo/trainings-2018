class Solution(object):
    def letterCasePermutation(self, S):
        l = [""]
        for k in range(len(S)):
            l2 = []
            if(S[k].isalpha()):
                for e in l:
                      l2.append(e+S[k].lower())
                    l2.append(e+S[k].upper())
                l = l2
            else:
                for i in range(len(l)):
                    l[i]+=S[k]
        return l