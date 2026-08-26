class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        for i in s:
            s1[i] = s1.get(i,0) + 1
        for i in t:
            s1[i] = s1.get(i,0) - 1
        return all(v == 0 for v in s1.values())
        
        
        