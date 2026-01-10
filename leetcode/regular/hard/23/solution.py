# https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        hp = []

        for i in range(len(lists)):
            if lists[i] is not None:
                heappush(hp, (lists[i].val, i))
        
        while hp:
            _, curr = heappop(hp)
            tail.next = lists[curr]
            tail = tail.next
            lists[curr] = lists[curr].next
            if lists[curr] is not None:
                heappush(hp, (lists[curr].val, curr))
        
        return dummy.next