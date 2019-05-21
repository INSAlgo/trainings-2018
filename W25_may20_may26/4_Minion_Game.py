string = input()
vowels = {'A', 'E', 'I', 'O', 'U'}
lenS = len(string)
scoreVowel = 0
scoreCons = 0
for pos in range(lenS):
    if string[pos] in vowels:
        scoreVowel += lenS - pos
    else:
        scoreCons += lenS - pos
if scoreCons > scoreVowel:
    print("Stuart", scoreCons)
elif scoreVowel > scoreCons:
    print("Kevin", scoreVowel)
else:
    print("Draw")
