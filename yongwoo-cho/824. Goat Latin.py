class Solution:
    def toGoatLatin(self, S: str) -> str:
        # a e i o u  : end with ma
        # consonant : move first to end , end with ma
        # sentence index 만큼 a
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        result = []
        for enum, s in enumerate(S.split(" ")):
            if s[0] in vowel:
                s = s + 'ma'
            else:
                s = s[1:] +s[0] + 'ma'
            
            s = s + 'a' * (enum+1)
            result.append(s)
        
        return " ".join(result)
            
                
                
            
            
