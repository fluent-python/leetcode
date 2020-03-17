class Solution:
    def myAtoi(self, str: str) -> int:
        remove_wh_str = str.lstrip()
        if len(remove_wh_str) == 0 or (len(remove_wh_str)==1 and not str.isdigit()): return 0

        negative_flag = False
        if remove_wh_str[0] == '-':
            negative_flag = True
            remove_wh_str = remove_wh_str[1:]
        elif remove_wh_str[0] == '+':
            remove_wh_str = remove_wh_str[1:]
        if not remove_wh_str[0].isdigit(): return 0

        result = []
        for x in remove_wh_str:
            if not x.isdigit(): break
            result.append(x)
        result = int(''.join(result))
        if result > pow(2, 31)-1:
            return -pow(2, 31) if negative_flag else pow(2, 31) -1

        return -result if negative_flag else result


if __name__ == '__main__':
    inputs = ["2147483648", "", "+1", "    -10", "42", "4193 with words", "words and 987", "-91283472332", "3.14159", "33 ww 22", ""]
    result = Solution().myAtoi(inputs[0])
    print(result)