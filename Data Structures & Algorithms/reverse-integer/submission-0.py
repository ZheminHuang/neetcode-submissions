class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1

        sign = -1 if x<0 else 1

        x= abs(x)

        result = 0

        while x:
            digit = x%10

            x//=10

            if result>INT_MAX//10:
                return 0
            
            if result == INT_MAX //10:
                limit_digit = 8 if sign ==-1 else 7

                if digit >limit_digit:
                    return 0
            result = result*10+digit
        
        result*=sign

        if result<INT_MIN or result>INT_MAX:
            return 0
        return result