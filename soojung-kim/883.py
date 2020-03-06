# 전처리: lower(), remove space, join
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.findall(r'\w+', s)
        s = ''.join(s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left+1, right-1
        return True


if __name__ == '__main__':
    result1 = Solution().isPalindrome("A man, a plan, a canal: Panama")
    result2 = Solution().isPalindrome("race a car")
    assert result1 == True and result2==False, "Wrong answer"