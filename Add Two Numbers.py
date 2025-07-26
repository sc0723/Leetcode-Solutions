# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        while l1 is not None:
            num1 += str(l1.val)
            l1 = l1.next
        
        num2 = ""
        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next

        
        num1 = int(num1[::-1])

        num2 = int(num2[::-1])


        res = num1 + num2
        res = str(res)[::-1]

        head = temp = ListNode()

        temp.val = int(res[0])
        for i in range(1, len(res)):
            curr = ListNode()
            curr.val = int(res[i])
            temp.next = curr
            temp = temp.next
        
        return head
        