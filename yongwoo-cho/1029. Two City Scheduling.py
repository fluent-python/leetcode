class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        result = 0
        subt_dict = {}
        N = len(costs) // 2
        
        for enum, cost in enumerate(costs):
            subt_dict[enum] = cost[0] - cost[1] 
        
        sorted_dict = sorted(subt_dict.items(),  key=(lambda x: x[1]))
        for enum, (k, v) in enumerate(sorted_dict):
            if enum < N:
                result += costs[k][0]
            else:
                result += costs[k][1]
        return result
            
