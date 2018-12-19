class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)<=1):   #cas avec un seul élément ou liste vide
            return len(nums)
        else:
            #grow=
            #1-> croissant
            #-1-> decroissant
            #0 -> constant (pour le début)
            grow = 0
            length = 1
            for i in range(1,len(nums)):
                diff = nums[i]-nums[i-1]
                if(grow == 0): #cas où le sens de variation est indéterminé, valeurs identiques au début
                    if(diff>0):
                        grow = 1
                        length+=1
                    elif(diff<0):
                        grow =- 1
                        length+=1
                else:
                    
                    if (grow == 1 and diff<0) or (grow == -1 and diff>0): #si on change de sens de variation
                        length+=1
                        grow = -grow #changer le sens de variation
                    #sinon c'est la dernière valeur qui est gardée dans la liste 
            return length