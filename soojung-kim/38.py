class Solution:
    def countAndSay(self, n: int) -> str:
        memo = "1"
        if n == 1:
            return memo
        for i in range(1, n):
            cnt = 1
            tmp = memo[0]
            tmp_memo = ""
            p = 0
            while p < len(memo) - 1:
                cur = memo[p + 1]
                if tmp != cur:
                    tmp_memo += str(cnt)
                    tmp_memo += tmp
                    cnt = 1
                    tmp = cur
                    p += 1
                    continue
                else:
                    cnt += 1
                p += 1
            memo = tmp_memo + str(cnt) + tmp
        return memo

