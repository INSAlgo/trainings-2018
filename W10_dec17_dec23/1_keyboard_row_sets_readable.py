class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        possible = []
        for word in words:
            for row in rows:
                for letter in word.lower():
                    if letter not in row:
                        break
                else:
                    possible.append(word)
                    break
        return possible
