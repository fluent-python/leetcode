class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        len_dict = {}
        max_num = 0
        
        for wall_row in wall:
            position = 0 
            for br in wall_row[:-1]:
                position += br

                t = len_dict.get(position)
                if t == None:
                    if max_num == 0:
                        max_num = 1
                    len_dict[position] = 1
                else:
                    len_dict[position] += 1
                    if t+1 > max_num:
                        max_num = t+1
        return len(wall) - max_num
