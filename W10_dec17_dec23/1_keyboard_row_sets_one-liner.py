class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        possible = [word for word in words
                    if [row for row in rows
                        if not [letter for letter in word.lower()
                                if letter not in row]]]
        return possible
