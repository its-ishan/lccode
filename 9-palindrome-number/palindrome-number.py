class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        leng = len(num_str)

        for i in range(leng//2):
            if(num_str[i]!=num_str[leng-i-1]):
                return False
        
        return True
       
          