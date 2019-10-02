class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        N = len(distance)
        total = sum(distance)
        result = 0 
        
        if start > destination:
            for i in range(destination, start):
                result += distance[i]
        else:
            for i in range(start, destination):
                result += distance[i]
        
        if total - result < result:
            return total - result
        else:
            return result
                
                
            
                
                
                
                
            
            
