class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        known = [2,4,8,16,32,64,128,256,512,1024]
        
        
        for div in known:
            while n > div:
                n = n / div
                if n % div != 0 :
                    return False
            if n == 1 or n == 2:
                return True
