# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists)>1:
            merged_lists = []

            for i in range(0,len(lists),2):
                list1=lists[i]

                if i+1 < len(lists):
                    list2=lists[i+1]
                else:
                    list2 =None
                
                merged = self.mergeTwoLists(list1,list2)
                merged_lists.append(merged)
            lists = merged_lists
        return lists[0]


    def mergeTwoLists(self, list1:Optional[ListNode], list2:Optional[ListNode])-> Optional[ListNode]:
        dummy=ListNode()
        current = dummy

        while list1 is not None and list2 is not None:
            if list1.val <=list2.val:
                current.next = list1
                list1=list1.next

            else:
                current.next = list2
                list2=list2.next
            current = current.next

        if list1 is not None:
            current.next = list1
        else:
            current.next = list2

        return dummy.next
            