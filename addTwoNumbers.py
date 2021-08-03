"""
题目：
给你两个非空的链表，表示两个非负的整数。他们每一位数字都是按照逆序的方式存储的，并且每位节点
只能存储一位数字，请你将两个数字相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字0之外，这两个数都不会以0开头。

示例1：
 2 -> 4 -> 3
 5 -> 6 -> 4
 -----------
 7 -> 0 -> 8
输入： l1 = [2, 4, 3], l2 = [5, 6, 4]
输出： [7, 0, 8]
解释： 342 + 465 = 807

示例2：
输入： l1 = [0]， l2 = [0]
输出： [0]

示例3：
输入： l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
输出： [8, 9, 9, 9, 0, 0, 0, 1]
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        h1, h2 = l1, l2
        tmp = 0
        while h1 or h2:
            val = h1.val + h2.val + tmp
            h1.val, tmp = val % 10, val // 10
            if not h1.next and h2.next: h1.next = ListNode(0)
            if not h2.next and h1.next: h2.next = ListNode(0)
            if not h1.next and not h2.next:
                if tmp: h1.next = ListNode(tmp)
                return l1
            h1 = h1.next
            h2 = h2.next


if __name__ == '__main__':
    a1 = ListNode(2)
    a2 = ListNode(4)
    a3 = ListNode(3)
    a1.next = a2
    a2.next = a3

    b1 = ListNode(7)
    b2 = ListNode(0)
    b3 = ListNode(8)
    b1.next = b2
    b2.next = b3

    s = Solution()
    res = s.addTwoNumbers(a1, b1)
