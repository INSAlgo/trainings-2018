class Solution(object):
   def isPerfectSquare(self, num):
       """
       :type num: int
       :rtype: bool
       """
       i = 1
       r = 0
       mini = 1
       maxi = num
       while(i != r):
           if(i**2 == num):
               return True
           if(i**2 < num):
               mini = i
           else:
               maxi = i
           r = i
           i = int((maxi + mini) / 2)
       return False
   
