class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nLen = len(needle)
        hLen = len(haystack)
        if nLen == 0:
            return 0

        for i in range(hLen):
            if needle == haystack[i:i+nLen]:
                return i

        return -1
