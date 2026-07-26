# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        group_prev = dummy

        while True:
            kth = self.getKth(group_prev,k)

            if kth is None:
                break
            
            group_next = kth.next

            previous = group_next
            current = group_prev.next

            while current is not group_next:
                next_node = current.next
                current.next = previous

                previous = current
                current = next_node

            old_group_start = group_prev.next
            group_prev.next = kth
            group_prev = old_group_start
        return dummy.next




    def getKth(self, current: Optional[ListNode], k: int) -> Optional[ListNode]:

        while current is not None and k>0:
            current = current.next
            k-=1
        return current
