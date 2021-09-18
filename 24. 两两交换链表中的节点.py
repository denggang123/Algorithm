class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead


head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

a = Solution().swapPairs(head1)
while a:
    print(a.val)
    a = a.next
