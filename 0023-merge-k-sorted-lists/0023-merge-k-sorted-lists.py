# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, l: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(l)==0:
            return None
        self.l = []
        def dfs(node):
            a = node.next
            self.l.append(node.val)
            if a is not None:
                dfs(a)
        for i in l:
            if i is None:
                pass
            else:
                dfs(i)
        self.l.sort()
        if len(self.l)==0:
            return None
        
        new = ListNode(self.l.pop(0))
        cur = new
        while self.l:
            cur.next = ListNode(self.l.pop(0))
            cur = cur.next
        return new