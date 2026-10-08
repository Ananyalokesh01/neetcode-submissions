class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for ch in s:
            if ch.isalnum():
                res+=ch.lower()
        x=list(res)
        left=0
        right=len(x)-1
        while left<right:
            x[left],x[right]=x[right],x[left]
            left+=1
            right-=1
        if "".join(x)==res:
            return True
        else:
            return False