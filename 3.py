class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, start, dic = 0, 0, {}

        for i, ch in enumerate(s):
            if ch in dic:
                if dic[ch] < start:
                    res = max(i-start+1, res)
                else:
                    start = dic[ch]+1
            else:
                res = max(i-start+1, res)
            dic[ch] = i

        return res
