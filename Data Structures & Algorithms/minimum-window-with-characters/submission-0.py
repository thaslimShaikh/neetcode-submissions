#Brute force approach
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        ans = ""
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j],0)+1
                valid = True 
                for ch in need:
                    if count.get(ch,0) < need[ch]:
                        valid = False 
                        break 
                if valid:
                    if ans =="" or (j-i+1)<len(ans):
                        ans=s[i:j+1]
                    break 
        return ans

    

