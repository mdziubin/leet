class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # Backtracking?

        def helper(left, right, tempStr):
            if right < left:
                return
            if not right and not left:
                res.append(tempStr)
                return
            if left:
                helper(left-1, right, tempStr + "(")
            if right:
                helper(left, right-1, tempStr + ")")
        helper(n, n, "")
        return res
