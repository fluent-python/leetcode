class Solution:
    def combination(self, n, r):
        if n-r < r :
            r = n-r
        
        denom = 1
        numer = 1
        for i in range(r):
            denom = denom * (n-i)
            numer = numer * (i+1)
        
        return int(denom/ numer)
            
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
            tmp = []
            for j in range(i+1):
                tmp.append(self.combination(i,j))
            output.append(tmp)
        # print(output)
        return output
