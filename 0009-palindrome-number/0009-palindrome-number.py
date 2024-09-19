class Solution(object):
    def isPalindrome(self, x):
        leng=len(str(x))
        y=str(x)
        for i in range(leng//2):
            if y[i]!=y[leng-i-1]:
                return False
            
                    
        
        return True

        