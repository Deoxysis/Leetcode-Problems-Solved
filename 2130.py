# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        #find length of list
        l = 1
        temp = head
        while(temp.next != None):
            l += 1
            temp = temp.next
        if l == 2: return head.val + head.next.val

        #traverse till l/2
        temp = head
        for i in range(l//2):
            temp = temp.next
        #reverse this half
        prev = None
        curr = temp
        while(curr != None):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        maxsum = 0
        front = head
        end = prev
        for i in range(l//2):
            val = end.val + front.val
            maxsum = max(val, maxsum)
            end = end.next
            front = front.next
        return maxsum

        