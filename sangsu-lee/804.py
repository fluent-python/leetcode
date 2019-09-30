from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        chars = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        char_dict = {chr(i): code for i, code in enumerate(chars, 97)}
        unique_codes = set()
        for word in words:
            string = ''
            for char in word:
                string += char_dict[char]
            unique_codes.add(string)
        return len(unique_codes)

s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

