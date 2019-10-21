class Solution:
    def romanToInt(self, s: str) -> int:
        symbol ={"0":10000,"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        
        
        before = "0"
        result = 0
        for sym in s:
            if symbol[before] < symbol[sym]:
                result += (symbol[sym] - 2 * symbol[before])
            else:
                result += symbol[sym]
            before  = sym
        return result
            
            
