class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_dict = {}
        pattern_dict = {}
        word_list = str.split(' ')
       
        print(word_list)
        
        if len(pattern) != len(word_list):
            print(len(pattern))
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in word_dict:
                if word_dict[pattern[i]] != word_list[i]:
                    return False
            else:
                word_dict[pattern[i]] = word_list[i]
    
            if word_list[i] in pattern_dict:
                if pattern_dict[word_list[i]] != pattern[i]:
                    return False
            else :
                pattern_dict[word_list[i]] = pattern[i]
                    
                    
        return True
