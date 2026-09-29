# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        left = head
        right = prev
        while right != None:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

            