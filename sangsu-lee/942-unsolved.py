from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        lp = rp = len([c for c in S if c == 'I'])
        ans_list = [i for i in range(len(S) + 1)]
        ans = [ans_list[lp]]
        for c in S:
            if c == 'I':
                rp += 1
                ans += [ans_list[rp]]
            if c == 'D':
                lp -= 1
                ans += [ans_list[lp]]
        return list(reversed(ans))



s = Solution()
print(s.diStringMatch("IDID"))
print(s.diStringMatch("III"))
