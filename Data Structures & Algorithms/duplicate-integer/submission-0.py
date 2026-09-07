class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq={}
        flag=0
        for num in nums:
            if num in freq:
                freq[num]=+1
                return True
            else:
                freq[num]=1
        return False