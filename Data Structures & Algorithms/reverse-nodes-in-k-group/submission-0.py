# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(cur,k):
            while cur and k:
                cur = cur.next
                k-=1
            return cur

        res = ListNode(0,head)
        prevGroup = res
        while True:
            kth = getKth(prevGroup,k)
            if not kth:
                break
            nxtGroup = kth.next
            
            prev,cur = nxtGroup,prevGroup.next
            while cur!=nxtGroup:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            temp = prevGroup.next
            prevGroup.next = prev
            prevGroup = temp
        return res.next