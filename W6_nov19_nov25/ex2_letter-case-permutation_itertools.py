from itertools import product

class Solution(object):
    def letterCasePermutation(self, S):
        ssets = [(letter.lower(), letter.upper())
                 if letter.isalpha() else (letter,)
                 for letter in S]

        li = list("".join(e) for e in product(*ssets))

        return li
