from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):  
        self.head = None








class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        ptr1 = l1; ptr2 = l2
        curr = temp; carry =0
        
        while ptr1 or ptr2:                 #while ptr1 or ptr2 is not null... at end of while loop we assing ptr1/ptr2 to ptr.next
           
            x = (l1.val if l1 != None else 0)  #ternary expression
            y = (l2.val if l2 != None else 0)
            s = x + y + carry
            carry = s//10
            curr.next = ListNode (s % 10)
            curr = curr.next
            if ptr1:
                ptr1 = ptr1.next
            if ptr2: 
                ptr2 = ptr2.next
                
            if carry:
                curr.next = ListNode(carry)
        
        return temp.next
    
# l1 = [2,4,3] 
# l2 = [5,6,4]


l1 = LinkedList()
l2 = LinkedList()

first_node = ListNode(2)
second_node = ListNode(4)
third_node = ListNode(3)

l1.head = first_node
first_node.next = second_node
second_node.next = third_node


first_node_2 = ListNode(5)
second_node_2 = ListNode(6)
third_node_2 = ListNode(4)

l2.head = first_node_2
first_node.next = second_node_2
second_node.next = third_node_2


Solution = Solution().addTwoNumbers(l1, l2)
print(Solution)