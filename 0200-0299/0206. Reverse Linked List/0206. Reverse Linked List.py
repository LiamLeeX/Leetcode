# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
        return new_head
# Iterative 
# Time O(n)
# Space O(1)


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head)

    def _reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self._reverse(n, node)

# Recursive 
# Time O(n)
# Space O(n) 递归函数调用栈


