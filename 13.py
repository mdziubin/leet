class Solution:
    def romanToInt(self, s: str) -> int:
        valMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        prev = 0
        for c in reversed(s):
            if valMap[c] < prev:
                total -= valMap[c]
            else:
                total += valMap[c]
            prev = valMap[c]
        return total
