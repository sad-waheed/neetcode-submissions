class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        temp = [[] for i in range(len(nums)+1)] 
        for key,val in d.items():
            temp[val].append(key)
        arr = []
        for i in range(len(temp)-1,0,-1):
            if not temp[i]: next
            arr.extend(temp[i])
            if len(arr) >= k: return arr 



        
        

