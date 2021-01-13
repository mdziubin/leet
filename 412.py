class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        self.stack = []

        def recFiz(num):
            s = ""
            if num % 3 == 0:
                s += "Fizz"
            if num % 5 == 0:
                s += "Buzz"
            if not s:
                s = str(num)
            self.stack.append(s)

        for i in range(1, n+1):
            recFiz(i)
        return self.stack
