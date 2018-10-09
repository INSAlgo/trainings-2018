class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # dp table
        m = [0] * (target + 1)
        
        # initialization
        m[0] = 1
        
        # bottom-up approach
        for i in range(target+1):
            for k in nums:
                if i-k >= 0:
                    m[i] += m[i-k]
        
        return m[target]
