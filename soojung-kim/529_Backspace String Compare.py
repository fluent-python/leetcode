class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s, t = [], []
        for i in S:
            if i != '#':
                s.append(i)
            if i == '#' and s:
                s.pop()
        for i in T:
            if i != '#':
                t.append(i)
            if i == '#' and t:
                t.pop()
        return ''.join(s) == ''.join(t)


if __name__ == '__main__':
    S = "#abc#"
    T = "c#d#"
    result = Solution().backspaceCompare(S, T)
    print(result)