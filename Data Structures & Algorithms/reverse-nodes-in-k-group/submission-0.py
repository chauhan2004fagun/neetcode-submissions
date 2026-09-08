# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        temp = head
        
        while temp:
            length += 1
            temp = temp.next

    
        pairs = length // k

    
        if pairs == 0:
            return head

    # Dummy node
        dummy = ListNode(0)
        dummy.next = head

    # Node before the current group
        group_prev = dummy

    # Step 2: Process every complete group
        for i in range(pairs):
            
            group_start = group_prev.next

        # Find last node of current group
            p = group_start

            for j in range(k - 1):
                p = p.next

        # p is the last node
        # Save the next group
            new_pair = p.next

        # Step 3: Reverse current group
            prev = new_pair
            current = group_start

            for j in range(k):
                next = current.next

                current.next = prev

                prev = current
                current = next

        # Step 4: Connect previous part to reversed group
            group_prev.next = p

        # Step 5: group_start is now the LAST node
        # of the reversed group
            group_prev = group_start

        return dummy.next