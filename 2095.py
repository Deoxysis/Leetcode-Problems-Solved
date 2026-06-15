# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        ptr = head
        while(ptr.next != None):
            length += 1
            ptr = ptr.next
        if length == 1: return None
        #traverse till mid
        prev = None
        curr = head
        for i in range( length//2):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        del curr
        return head


#slow fast pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow_ptr = head
        fast_ptr = head
        prev = None
        while(fast_ptr != None and fast_ptr.next is not None):
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        prev.next = slow_ptr.next
        del slow_ptr
        return head
