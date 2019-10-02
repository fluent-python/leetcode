class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        check_dict = {}
        result = 0 
        for dom in dominoes:
            if dom[0] > dom[1]:
                input_t = (dom[1],dom[0])
            else:
                input_t = (dom[0], dom[1])
                
            if input_t in check_dict:
                check_dict[input_t] +=1
            else :
                check_dict[input_t] = 1
        
        #calc
        for k, v in check_dict.items():
            if v > 1 :
            
                result += ((v*(v-1))//2)
                
        return result
                
