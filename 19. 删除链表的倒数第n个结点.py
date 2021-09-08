# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node_num = 0
        node = head
        while node:
            node_num += 1
            node = node.next
        ptr = head
        for i in range(node_num):
            if node_num - i == n:
                if i == 0:
                    head = head.next
                else:
                    for j in range(i):
                        if j == i - 1:
                            ptr.next = ptr.next.next
                        else:
                            ptr = ptr.next
                break
        return head


a = ListNode(5)
b = ListNode(4, next=a)
c = ListNode(3, next=b)
d = ListNode(2, next=c)
e = ListNode(1, next=d)

s = Solution()
res = s.removeNthFromEnd(e, 2)
while res:
    print(res.val)
    res = res.next
