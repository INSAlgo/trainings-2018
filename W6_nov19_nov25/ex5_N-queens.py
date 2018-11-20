class Solution(object):
    def recur (self, pos, d,n):
        if d==n:
            return 1 #profondeur max atteinte
        cpt = 0
        for k in range(n):
            ok = 1
            for i in range(len(pos)):
                if(abs(pos[i]-k)==abs(i-d) or pos[i]==k):
                    ok = 0
            if ok: #aucune autre reine ne rentre en conflit
                cpt+=self.recur(pos+[k],d+1,n)
        return cpt
            
    def totalNQueens(self, n):
        return self.recur([],0,n) 