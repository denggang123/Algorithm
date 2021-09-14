class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: [ListNode]):

        res = ListNode()
        p = res
        while True:
            min_val = float("inf")
            index = 0
            for i, item in enumerate(lists):
                if not item:
                    continue
                if item.val < min_val:
                    min_val = item.val
                    index = i
            if min_val == float("inf"):
                break
            p.next = lists[index]
            p = p.next
            lists[index] = lists[index].next

        return res.next


def gen_linklist(lst):
    if not lst:
        return None
    res = ListNode(lst[0])
    p = res
    for item in lst[1:]:
        p.next = ListNode(item)
        p = p.next
    return res


if __name__ == '__main__':
    lis = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linklists = []
    for item in lis:
        linklists.append(gen_linklist(item))
    a = Solution().mergeKLists(linklists)
