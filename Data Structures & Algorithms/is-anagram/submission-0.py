class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        req={}
        for x in s:
            freq[x] = freq.get(x, 0) + 1
        for y in t:
            req[y] = req.get(y, 0) + 1
        if freq==req:
            return True 
        else:
            return False