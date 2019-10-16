class Solution:
    def longestWord(self, words: List[str]) -> str:
        result = ""
        words.append("")
        words.sort()
        for enum, word in enumerate(words):
            if word[:-1] in words:
                if len(result) < len(word):
                    result = word
                elif len(result) == len(word) and result > word:
                    result = word
            else:
                words[enum] = ""
        return result
                    
