# Definition for singly-linked list.
# Intuition
# We’re given two non-empty linked lists representing two non-negative integers, where each node contains a single digit and the digits are stored in reverse order.

# We need to add the two numbers digit by digit, just like how you do addition by hand — carry over if the sum of two digits ≥ 10.

# ✅ Traverse both lists together, add corresponding digits and carry, create a new node for each digit of the result.
# ✅ If a carry remains at the end, add an extra node


## Important to review linked lists in python, head should always be remembered through a memory pointer.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        # Run loop while l1 exists, OR l2 exists, OR we still have a carry
        while l1 is not None or l2 is not None or carry != 0:
            # Get values safely (use 0 if node is None)
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            
            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            
            # Create the NEXT node with the digit
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Advance pointers if possible
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        return dummy_head.next
    
if __name__ == "__main__":
    l1 = ListNode(2, next=ListNode(4, ListNode(3)))
    l2 = ListNode(5, next=ListNode(6, ListNode(4)))
    sol_nodes= Solution().addTwoNumbers(l1,l2)
    print("Solution")
    while sol_nodes:
        print(sol_nodes.val)
        sol_nodes = sol_nodes.next