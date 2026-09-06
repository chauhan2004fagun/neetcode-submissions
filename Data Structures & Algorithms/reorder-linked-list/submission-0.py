# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        while not head.next or not head.next.next:
            return 
        m=e=head
        while e.next and e.next.next:
            e = e.next.next
            m = m.next
        # make p2 pointer and end break the node at mnext
        p2 = m.next
        m.next = None
        # reverse the last list starting from p2 
        prev = None
        while p2 and p2.next:
            p2next = p2.next
            p2.next = prev
            prev = p2
            p2 = p2next
        p2.next = prev
        # merge the list 
        p1 = head
        while p1 and p2:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p2.next = p1next
            p1 = p1next
            p2 = p2next