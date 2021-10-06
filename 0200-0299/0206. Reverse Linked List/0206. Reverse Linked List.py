# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        while head is not None:
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node
        return new_head

# head -> head.next
