class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(' ')
        ans = []
        for i, word in enumerate(words):
            assert isinstance(word, str)
            if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
                word += 'ma'
            else:
                firstword = word[0]
                word = word[1:]
                word += (firstword + 'ma')
            word += 'a'*(i+1)
            ans.append(word)
        return ' '.join(ans)


s = Solution()
print(s.toGoatLatin("I speak Goat Latin"))
