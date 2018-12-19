class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sd_numbers = []
        for num in range(left, right + 1):
            # Construct a set of the digits of the number
            digits = set([int(d) for d in str(num)])

            # Check that the number is divisible by every digit
            if 0 in digits:
                divisible = False
            else:
                divisible = True
                for d in digits:
                    if num % d != 0:
                        divisible = False

            # If the number passed the test for all digits, add it to the list
            if divisible:
                sd_numbers.append(num)

        return sd_numbers
