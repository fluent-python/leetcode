class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def calc_area(a,b,c):
            return abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(a[0]*c[1]+c[0]*b[1]+b[0]*a[1])) /2
             
            
                
            
        max_area = 0 
        p_len = len(points)
        for i in range(p_len-2):
            for j in range(i,p_len-1):
                for k in range(j, p_len):
                     if max_area <calc_area(points[i],points[j], points[k]):
                            max_area  =calc_area(points[i],points[j], points[k])
        
        return max_area
