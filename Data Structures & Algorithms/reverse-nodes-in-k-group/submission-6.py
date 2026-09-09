# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len = 0
        current = head
        while current:
            len += 1
            current = current.next
        pairs = len // k

        if pairs == 0:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        for i in range(pairs):
            group_start = group_prev.next
            p = group_start

            for j in range(k-1):
                p = p.next

            new_pair  = p.next

            prev = None
            prev = new_pair
            current = group_start
            
            for j in range(k):
                cnext = current.next
                current.next = prev
                prev = current
                current = cnext
            group_prev.next = p

            group_prev = group_start
        return dummy.next