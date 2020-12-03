class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        shortest = min(strs, key=len)
        if shortest == "":
            return ""
        for i, ch in enumerate(shortest):
            for string in strs:
                if string[i] != ch:
                    return shortest[:i]
        return shortest
