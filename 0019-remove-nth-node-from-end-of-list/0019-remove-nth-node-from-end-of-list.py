# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        cnt = 0
        curr = head
        while curr != None:
            cnt += 1
            curr = curr.next
        b = cnt - n
        if b == 0:
            return head.next
        
        curr = head
        for i in range(b-1):
            curr = curr.next
        curr.next = curr.next.next
        return head