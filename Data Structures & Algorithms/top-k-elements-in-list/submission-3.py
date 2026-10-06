class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        result=[]
        for num in nums:
            freq[num]= freq.get(num,0)+1
        arr=list(freq.keys())
        arr.sort(key=lambda x: freq[x], reverse=True)
        return arr[:k]           


        

        