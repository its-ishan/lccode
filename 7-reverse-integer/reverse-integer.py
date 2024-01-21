class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT = 2 ** 31 - 1 # 2,147,483,647
        MIN_INT = -2 ** 31    #-2,147,483,648
        ans=0
        while(x != 0):
            if ans > MAX_INT / 10 or ans < MIN_INT / 10:
                return 0
            rem = x%10 if x > 0 else x % -10
            ans = ans*10+rem
            x = math.trunc(x/10)
        return ans
        