class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        #Iterate through all numbers from `left` to `right` and only keep those who are self dividing.
        return [i for i in range(left, right+1) if self.isSelfDividing(i)]

        # One liner : return [num for num in range(left, right+1) if all([int(i) != 0 and num % int(i) == 0 for i in str(num)])]

    # Check if a `num` is selfDividing
    def isSelfDividing(self, num):
        return all([int(i) != 0 and num % int(i) == 0 for i in str(num)])

