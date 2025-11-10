class Solution:
    
    def fun(self, n):
        s = 0
        while n > 0:
            d = n % 10
            s = s + d ** 2
            n = n // 10
        
        return s
        
    def isHappy(self, n: int) -> bool:
        count = 0
        while count < 10:
            n = self.fun(n)
            if n == 1:
                return True

            count += 1
            
        return False
            
        