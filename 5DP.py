class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        max_len = 0
        n = len(s)
        DP = [[0 for x in range(n)] for y in range(n)]
        for i in range(n):
            DP[i][i] = True
            max_len = 1
            ans = s[i]
        for i in range(n-1):
            if s[i] == s[i+1]:
                DP[i][i+1] = True
                ans = s[i:i+2]
                max_len = 2
        for j in range(2, n):
            for i in range(0, j-1):
                if s[i] == s[j] and DP[i+1][j-1]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j+1]
                        max_len = j - i + 1
        return ans
