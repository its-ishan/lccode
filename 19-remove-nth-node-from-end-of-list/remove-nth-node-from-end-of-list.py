# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0

        while current is not None:
            current = current.next
            length +=1

        if length == n:
            temp = head.next
            del head
            return temp
        
        current = head
        dummy = ListNode(0)
        temp = dummy

        steps = length - n
        for i in range(steps):
            temp.next = current
            temp = temp.next
            current = current.next

        next_node = current.next
        del current
        temp.next = next_node

        return dummy.next
            

        