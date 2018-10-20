class Solution:
    def dist(self,p1,p2):
        return ((p1[0]-p2[0])**2 +(p1[1]-p2[1])**2) #retourne la distance au carré entre deux points
    def verif(self,pRef,dRef,lP):
        adjacent=0
        diag=0
        for p in lP:
            d=self.dist(pRef,p)
            if d==dRef :
                adjacent+=1
            elif d==2*dRef :
                diag+=1
            
        if(adjacent==2 and diag==1):return True #deux sommets éloignés de la longueur du côté, un éloigné de la distance de la diagonale
        return False
                
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        l=[p1,p2,p3,p4]
        dRef=min(self.dist(p1,p2),self.dist(p1,p3)) #taille du côté si c'est bien un carré
        for k in range(len(l)):
            if(not self.verif(l[k],dRef,l[:k]+l[k+1:])):return False
        return True