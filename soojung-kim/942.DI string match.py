class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        N = [elm for elm in range(len(S) + 1)]
        result = []

        for i in S:
            value = N[0] if i == 'I' else N[-1]
            N.remove(value)
            result.append(value)
        result.append(N[0])
        return result
