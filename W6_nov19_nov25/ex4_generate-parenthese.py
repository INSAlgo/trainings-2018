class Solution(object):
    def BK(self,s,cpt,n,l):
        if(len(s)==n*2 and cpt==0):
            l.append(s)
        elif(cpt>=0 and cpt<=2*n-len(s)):
            self.BK(s+"(",cpt+1,n,l)
            self.BK(s+")",cpt-1,n,l)
    def generateParenthesis(self, n):
        l = []
        self.BK("",0,n,l)
        return l
        