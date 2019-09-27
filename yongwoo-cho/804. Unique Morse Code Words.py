class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
    
        def get_morse(alpha_string):
            table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
            tmp=""
            for idx in range(len(alpha_string)):
                t = table[ord(alpha_string[idx]) - ord("a")]
                tmp+=t
                
            print(tmp)
            return tmp 
        
        morse_dict = {}
        unique = 0 
        for let in words:
            m = get_morse(let)
            if m not in morse_dict:
                unique += 1
                morse_dict[m] = 1
        return unique
                
                
                
            
        
