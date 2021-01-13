class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        newWord = True
        for c in s:
            if c != " " and newWord:
                newWord = False
                count += 1
            elif c == " ":
                newWord = True
        return count
