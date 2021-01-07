# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev = ListNode(0,head)
        newHead = head.next
        
        slow = fast = head
        while slow and slow.next:
            fast = slow.next
            temp = fast.next
            
            slow.next = fast.next
            fast.next = slow
            prev.next = fast
            prev = slow
            
            slow = temp
        return newHead