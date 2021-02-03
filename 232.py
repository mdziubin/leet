class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for _ in range(len(self.q1)-1):
            self.q2.append(self.q1.pop())
        ret = self.q1.pop(0)
        for _ in range(len(self.q2)):
            self.q1.append(self.q2.pop())
        return ret

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.q1[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.q1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
