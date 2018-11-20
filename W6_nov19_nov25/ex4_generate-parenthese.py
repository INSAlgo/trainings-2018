class Solution(object):
    def BK(self, s, cpt, n, li):
        if(len(s) == n * 2 and cpt == 0):
            li.append(s)
        elif(cpt >= 0 and cpt <= 2 * n - len(s)):
            self.BK(s + "(", cpt + 1, n, li)
            self.BK(s + ")", cpt - 1, n, li)

    def generateParenthesis(self, n):
        li = []
        self.BK("", 0, n, li)
        return li
