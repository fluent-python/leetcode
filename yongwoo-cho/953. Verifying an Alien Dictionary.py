class Solution:

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        def check_valid(a,b):
            print(a,b)
            for i in range(min(len(a),len(b))):
                if a[i] > b[i]:
                    return False
                elif a[i] < b[i]:
                    return True
            if len(a) > len(b):
                return False
            
            return True
        
        order = list(order)
        before = None
        for word in words:
            tmp = []
            for idx,w in enumerate(list(word)):
                tmp.append(order.index(w)+1)
            if before == None:
                before  = tmp
            else:
                result = check_valid(before, tmp)
                if result == False:
                    return False
                before  = tmp
        return True
                
            
                
