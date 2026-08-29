class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            arr = [0] * 26
            for i in s:
                arr[ord(i) - ord('a')] += 1
            arr = tuple(arr)
            val = d.get(arr,[])
            val.append(s)
            d[arr] = val
        arr = []
        for k,v in d.items():
            arr.append(v)
        return arr
        
        