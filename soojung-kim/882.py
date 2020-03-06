class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        return False


if __name__ == '__main__':
    result = Solution().isAnagram(s = "rat", t = "car")
    print(result)