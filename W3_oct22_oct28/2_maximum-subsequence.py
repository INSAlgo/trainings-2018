from collections import defaultdict


def longest_incr(sequence):
    nb_lenseq = defaultdict(int)
    for nb in sequence:
        nb_lenseq[nb] = max(nb_lenseq[nb], nb_lenseq[nb - 1] + 1)
    nbm = None
    for nb in nb_lenseq:
        if nbm is None or nb_lenseq[nb] > nb_lenseq[nbm]:
            nbm = nb
    return range(nbm - nb_lenseq[nbm] + 1, nbm + 1)


n = int(input())
sequence = list(map(int, input().split()))
print(" ".join(map(str, longest_incr(sequence))))
