class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        A={}
        B={}
        for x in s:
            A[x] = A.get(x, 0) + 1
        for y in t:
            B[y] = B.get(y, 0) + 1
        if A==B:
            return True 
        else:
            return False