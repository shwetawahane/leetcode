class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        l = len(needle)
        i = 0
        while(i<len(haystack)):
            if(haystack[i:i+l]==needle):
                return i
            i+=1
        return -1
        
