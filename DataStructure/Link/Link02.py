#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：Link02.py
@Author  ：WL
@Date    ：2022/7/28 11:08 
@Describe: 初始链表
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

print(a.next.val)
print(a.next.next.val)

