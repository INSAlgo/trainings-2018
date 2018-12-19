class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic={} #stocker le nombre d'occurences de chaque caractere 
        for c in s:
            if c in dic:#important de commencer par le cas où la lettre est déjà dans le dic (compéxité meilleure en moyenne)
                dic[c]+=1
            else:
                dic[c] = 1
        l=sorted(dic.keys(),key = lambda x:-dic[x]) #trier les clés en fonction du nombre d'occurences dans la chaine, en sens décroissant
        result = ""
        for c in l:
            result+=c*dic[c] #recomposer la chaine
        return result