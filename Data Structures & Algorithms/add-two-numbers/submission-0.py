# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1,p2 = l1,l2
        carry = 0
        res = ListNode()
        cur = res

        while p1 or p2 or carry:
            node = ListNode()
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            n = val1+val2+carry
            if n < 10:
                node.val = n
                carry = 0
            else:
                carry = 1
                node.val = n%10
            cur.next = node
            cur = cur.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        
        return res.next