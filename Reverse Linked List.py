# Definition for singly-linked list.
class ListNode:
    """
    USED TO IMPLEMENT THE LINKED LIST DATA STRUCTURE.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    """
    USED TO IMPLEMENT THE LINKED LIST DATA STRUCTURE.
    """
    def __init__(self, start_list=None) -> None:

        self._head = ListNode(None)

        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        out = 'SLL ['
        node = self._head       
        while node:
            out += str(node.val)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def insert_back(self, value: object) -> None:
       
        new_Node = ListNode(value)            # create new node
       
        prev = None                         
        curr = self._head                   # start at front sentinel

        while curr is not None:             # iterate through list until curr is NONE and prev is the LAST NODE
            prev = curr 
            curr = curr.next     
                       
        prev.next = new_Node                # once curr is NONE, link new node to the LAST NODE's next variable       
        
    def get_head(self):
        return self._head
    
    def set_head(self, new_head):
        self._head = new_head
      
      
class Solution:
    """
    lEETCODE SOLUTION IS HERE.  CODE ABOVE IS USED TO IMPLEMENT THE LINKED LIST DATA STRUCTURE.
    """
    def reverseList(self, head):
        
        prev, curr = None, head
        
        while curr:
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext
        
        return prev
    
    def reverseList_RECURSIVE(self, head):
        
        # FOR AN EMPTY LINKED LIST
        if not head:
            return None
        
        newHead = head
        
        if head.next:
            newHead = self.reverseList_RECURSIVE(head.next)
            head.next.next = head
        head.next = None
        
        # BASE CASE
        return newHead
        
    
  
  
  
def main():  
    nums = [1,2,3,4,5]
    nums2 = [1]
    

    # TEST ITERATIVE (TWO POINTER METHOD)
    LList = LinkedList()
    for number in nums:
        LList.insert_back(number)
        

    print(LList)
    head = LList.get_head()

    new_list = Solution().reverseList(head)     # expected: [5, 4, 3, 2, 1]
    LList.set_head(new_list)
    print(LList)




    # TEST RECURSIVE METHOD
    LList = LinkedList()
    for number in nums:
        LList.insert_back(number)
        
    print(LList)
    head = LList.get_head()

    new_list = Solution().reverseList_RECURSIVE(head)     # expected: [5, 4, 3, 2, 1]
    LList.set_head(new_list)
    print(LList)
    
    
    
    # TEST RECURSIVE METHOD 2
    LList = LinkedList()
    for number in nums2:
        LList.insert_back(number)
        
    print(LList)
    head = LList.get_head()

    new_list = Solution().reverseList_RECURSIVE(head)     # expected: [1 -> None]
    LList.set_head(new_list)
    print(LList)
    
    
    
    # TEST RECURSIVE METHOD 3
    LList = LinkedList()
        
    print(LList)
    head = LList.get_head()

    new_list = Solution().reverseList_RECURSIVE(head)     # expected: [5, 4, 3, 2, 1]
    LList.set_head(new_list)
    print(LList)
    
if __name__ == "__main__":
    main()