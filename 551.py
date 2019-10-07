class Solution:
    def checkRecord(self, s: str) -> bool:
        if 'LLL' in s:
            return False
        if s.count('A') >= 2:
            return False
        return True
