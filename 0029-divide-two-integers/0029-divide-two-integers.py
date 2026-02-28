class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
      
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
       
        negative = (dividend < 0) ^ (divisor < 0)
        
   
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
      
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                result += 1 << i
                dividend -= divisor << i
        
        return -result if negative else result