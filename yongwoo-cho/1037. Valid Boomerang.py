class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # 동일한 점에 있는 경우
        if points[0] == points[1] or points[1] == points[2] or points[0]== points[2]:
            return False
        
        # 기울기 벡터가 같으면 일직선       
        if (points[0][1] - points[1][1]) == 0:
            if (points[0][1] - points[2][1]) == 0 :
                return False
            else :
                return True
        if (points[0][1] - points[2][1]) == 0 :
            if (points[0][1] - points[1][1]) == 0:   
                return False
            else :
                return True
        
        slope_v1 = (points[0][0] - points[1][0]) / (points[0][1] - points[1][1])
        slope_v2 = (points[0][0] - points[2][0]) / (points[0][1] - points[2][1])
        
        
        if (slope_v1) == (slope_v2):
            return False
        else:
            return True
