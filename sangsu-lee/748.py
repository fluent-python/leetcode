import copy
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        all_chars_in_lp = [c.lower() for c in list(licensePlate) if c.isalpha()]
        print(all_chars_in_lp)
        cnt_dict = {}
        for char in all_chars_in_lp:
            if char in cnt_dict:
                cnt_dict[char] += 1
            else:
                cnt_dict[char] = 1
        for word in words:
            char_list = list(copy.deepcopy(word))
            if self.is_valid_word(char_list, cnt_dict):
                return word

    def is_valid_word(self, char_list, cnt_dict):
        for k, v in cnt_dict.items():
            for _ in range(v):
                if k in char_list:
                    char_list.remove(k)
                else:
                    return False
        return True
s = Solution()
s.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"])
