class Solution:
    def romanToInt(self, s: str) -> int:
        rom2idx = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        int_list = [rom2idx[roman] for roman in s]
        result = 0
        i = 0
        while i<len(int_list):
            cur = int_list[i]
            try:
                cur_next = int_list[i+1]
            except IndexError:
                cur_next = 0
            if cur >= cur_next:
                result += cur
                i += 1
            else:
                result += cur_next - cur
                i += 2
        return result


if __name__ == '__main__':
    inputs = ['III', 'MCMXCIV', "MDCXCV"]
    true = [3, 1994, 1695]
    for i in range(len(inputs)):
        result = Solution().romanToInt(inputs[i])
        assert result == true[i], "Wrong answer: inputs is \"{}\"".format(inputs[i])