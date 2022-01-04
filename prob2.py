# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Str = ""
        while (l1.next != None):
            l1Str += str(l1.val)
            l1 = l1.next
            if(l1.next == None):
                l1Str += str(l1.val)
                break

        l2Str = ""
        while (l2.next != None):
            l2Str += str(l2.val)
            l2 = l2.next
            if(l2.next == None):
                l2Str += str(l2.val)
                break

        l1Str = l1Str[::-1]

        l2Str = l2Str[::-1]
        
        
        
        
        
        
        
        l1Int = int(l1Str)
        l2Int = int(l2Str)

        total = l1Int + l2Int

        strTotal = str(total)

        strTotal = strTotal[::-1]

        nodes = []

        for i in range(len(strTotal)):
            l3 = ListNode(int(strTotal[i]))
            nodes.append(l3)

        head = nodes[0]

        curr = head

        for i in range(len(nodes)):
            if(i != len(nodes) - 1):
                curr.next = nodes[i+1]

        return head
            
