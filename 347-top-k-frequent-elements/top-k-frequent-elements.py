class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {x:0 for x in nums}
        for i in nums:
            dict1[i] += 1
            
        a = sorted(dict1, key=dict1.get,reverse=True)

        return a[:k]
