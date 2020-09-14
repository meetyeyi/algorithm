# -*- coding: utf-8 -*-


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 输入一个链表，反转链表后，输出新链表的表头。


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            temp = pHead.next
            pHead.next = last
            last = pHead
            pHead = temp
        return last
