# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0

        i = 0
        while l1:
            sum += l1.val*10**i
            l1 = l1.next
            i += 1

        i = 0
        while l2:
            sum += l2.val*10**i
            l2 = l2.next
            i += 1

        if sum == 0:
            return ListNode(0)

        dummy = cur = ListNode()
        while sum:
            cur.next = ListNode(sum % 10)
            cur = cur.next
            sum //= 10

        return dummy.next
