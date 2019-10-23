class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        queue = []

        check_color = image[sr][sc]
        
        if newColor == check_color:
            return image
        queue.append([sr,sc])
        

        
        while len(queue) > 0 :
            t = queue.pop()
            image[t[0]][t[1]] = newColor
            
            for i in range(4):
                new_x = t[0] + dx[i]
                new_y = t[1] + dy[i]
                if (0 <= new_x < len(image)) and (0 <= new_y < len(image[0])):
                    if image[new_x][new_y] == check_color:
                            queue.append([new_x,new_y])
                        
        return image
                    
        
