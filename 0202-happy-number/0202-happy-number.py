class Solution:
    def isHappy(self, n: int) -> bool:
    
        def fun(n):
            sum = 0
            while n > 0:
                d = n % 10
                sum += d ** 2
                n = n // 10
            return sum 
     
        
        slow = n
        fast = fun(n)
      
        while fast != 1 and slow != fast:
            slow = fun(slow)
            fast = fun(fun(fast))

        return fast == 1
            
        