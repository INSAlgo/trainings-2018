class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic={} #stocker le nombre d'occurences de chaque caractere 
        for c in s:
            if c in dic:#important de commencer par le cas o� la lettre est d�j� dans le dic (comp�xit� meilleure en moyenne)
                dic[c]+=1
            else:
                dic[c] = 1
        l=sorted(dic.keys(),key = lambda x:-dic[x]) #trier les cl�s en fonction du nombre d'occurences dans la chaine, en sens d�croissant
        result = ""
        for c in l:
            result+=c*dic[c] #recomposer la chaine
        return result