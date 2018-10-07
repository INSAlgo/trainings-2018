class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])

        maxcol = [max(grid[i][j] for i in range(h)) for j in range(w)]
        maxlin = [max(grid[i][j] for j in range(w)) for i in range(h)]

        return sum(sum(min(maxcol[j], maxlin[i]) - grid[i][j]
                       for j in range(w))
                   for i in range(h))
