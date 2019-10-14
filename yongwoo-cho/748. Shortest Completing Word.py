class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        letter_plate = []
        result = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        for l in licensePlate.lower():
            if "a" <= l <= "z":
                letter_plate.append(l)
        
        for word in words:
            count = 0
            w_list = list(word)
            for lp in letter_plate:
                if lp in w_list:
                    count += 1
                    w_list.remove(lp)
                else:
                    break;
            if count == len(letter_plate):
                if len(result) > len(word):
                    result = word
        
        return result
            
            
                
                
                    
            
            
                    
