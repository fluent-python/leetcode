class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        select = {}
        interest ={}
        
        
        for idx, a in enumerate(list1):
            select[a] = idx
        
        for idx, b in enumerate(list2):
            if b in select:
                interest[b] = select[b] + idx
        
        least_sum = 3000
        
        for k,v in interest.items():
            print(k,v)
            if v < least_sum:
                result = [k]
                least_sum = v
            elif v == least_sum:
                result.append(k)
        return result
                
                
            
            
            
