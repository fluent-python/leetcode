class Solution:
    def isHappy(self, n: int) -> bool:
        already = {n}
        
        num = n
        while True:
            split_number = str(num)
            num = 0 
            for digit in split_number:
                num += (int(digit)**2)
            print(num)
            if num == 1:
                return True
            if num in already:
                return False
            else:
                already.add(num)
                
            
            
            
