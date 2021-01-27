class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking
        if not digits: return []
        res = []
        d = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.helper(digits, "", res, d)
        return res
    
    def helper(self, digits, curr, res, d):
        if not digits:
            res.append(curr)
            return
        for c in d[int(digits[0])-2]:
            self.helper(digits[1:], curr+c, res, d)