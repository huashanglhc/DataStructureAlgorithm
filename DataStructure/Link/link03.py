#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：link03.py
@Author  ：WL
@Date    ：2022/7/28 11:21 
@Describe: 链表操作
"""


class Node:
    """定义节点类"""
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class SingleLinkList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def traverse(self):
        cur = self.head
        while cur is not None:
            print(cur.val, end=' ')
            cur = cur.next
        print()

    def reverse(self):
        """反转单链表非递归求解"""
        prev = None
        cur = self.head
        while cur is not None:
            cur_next = cur.next
            cur.next = prev
            prev = cur
            cur = cur_next
        return prev
