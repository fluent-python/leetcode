from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n+1):
            val = str(i)
            if i % 15 == 0 :
                val ='FizzBuzz'
            elif i % 5 == 0:
                val = 'Buzz'
            elif i % 3 == 0:
                val = 'Fizz'
            result.append(val)
        return result


if __name__ == '__main__':
    result = Solution().fizzBuzz(15)
    print(result)