class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        length=(len(nums)//3)
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for num in freq:
            if freq[num]>length:
                res.append(num)
        return res        