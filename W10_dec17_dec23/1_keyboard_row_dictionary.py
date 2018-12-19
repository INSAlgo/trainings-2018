class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiopQWERTYUIOP", "asdfghjklASDFGHJKL", "zxcvbnmZXCVBNM"]
        dico = {letter: row_nb for row_nb in range(3)
                for letter in rows[row_nb]}
        possible = []
        for word in words:
            for i in range(1, len(word)):
                if dico[word[i]] != dico[word[i - 1]]:
                    break
            else:
                possible.append(word)
        return possible
