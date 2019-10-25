# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binary_search(left,right):
            t = (left+right) // 2
            if left == right:
                return left
            
            if isBadVersion(t):
                return binary_search(left,t)
            else:
                return binary_search(t+1, right)
                
        return binary_search(1,n)
        
                
                
