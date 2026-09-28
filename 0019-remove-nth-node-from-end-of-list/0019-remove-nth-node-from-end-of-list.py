# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        p1 = head
        p2 = head
        for i in range(n):
            p2 = p2.next
        if p2 == None:
            head = head.next
            return head
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        p1.next = p1.next.next
        return head






        # cnt = 0
        # curr = head
        # while curr != None:
        #     cnt += 1
        #     curr = curr.next
        # b = cnt - n
        # if b == 0:
        #     return head.next
        
        # curr = head
        # for i in range(b-1):
        #     curr = curr.next
        # curr.next = curr.next.next
        # return head