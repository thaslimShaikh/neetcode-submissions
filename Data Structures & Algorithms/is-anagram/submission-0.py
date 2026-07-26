class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        freqS = {}
        freqT = {}
        for x in s:
            freqS[x] = freqS.get(x,0)+1
        for y in t:
            freqT[y] = freqT.get(y,0)+1
        return freqS == freqT