# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()  # dummy node is object that calls the class constructor
        cur = dummy  # postion to insert new node
        carry = 0  # maintain a carry variable

        while l1 or l2 or carry:  # iterate until both null
            v1 = (
                l1.val if l1 else 0
            )  # set the values if node exists, else set it as null
            v2 = l2.val if l2 else 0
            # new digit
            val = v1 + v2 + carry
            # but if it has a carry(it is a 2 digit number)
            carry = val // 10  # // is float division operator
            val = val % 10
            # appent to linked list
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            # we are not done yet, consider 8+7, we need to account for carry
            # run loop until carry is also 0
        return dummy.next
