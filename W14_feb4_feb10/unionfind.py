#!/usr/bin/env python3

##############################################################################
#                        Louis Sugy 2019, MIT license                        #
#                                for INSAlgo                                 #
##############################################################################


class UnionFind:
    """An implementation of a Union-Find data structure for hashable types.
       All the elements are given at the start and this class supports only
       the union and find operations, as well as checking if two elements
       belong to the same set.
       These 3 operations have a time complexity O(a(n)), where a is the
       inverse Ackermann function, such that a(n) < 5 for any n that can be
       written in this physical universe.
    """

    def __init__(self, singletons):
        """Initialize the data structure with the elements of the given
           iterable as singletons.
        """
        self.parents = {e: e for e in singletons}
        self.rank = {e: 0 for e in singletons}

    def find(self, e):
        """Return the root of the tree containing the given element, or None
           if the element cannot be found. Applies path compression.
        """
        if e not in self.parents:
            return None
        if self.parents[e] != e:
            self.parents[e] = self.find(self.parents[e])
        return self.parents[e]

    def union(self, e1, e2):
        """Merge the sets containing the elements e1 and e2, by rank.
        """
        r1, r2 = self.find(e1), self.find(e2)
        if r1 == r2:  # The elements are already in the same set
            return
        # We choose that r1 will be the root with highest rank
        if self.rank[r1] < self.rank[r2]:
            r1, r2 = r2, r1
        # We choose r1 as the parent of r2 and update r1's rank
        self.parents[r2] = r1
        if self.rank[r1] == self.rank[r2]:
            self.rank[r1] += 1

    def is_same_set(self, e1, e2):
        """Determines whether e1 and e2 are in the same set.
        """
        return (self.find(e1) == self.find(e2))
