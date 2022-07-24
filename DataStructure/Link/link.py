#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：link.py
@Author  ：WL
@Date    ：2022/6/20 21:41 
@Describe: 链表
"""


class Nodes:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def reverse(head):
        cur_node = head
        new_link = None
        while cur_node is not None:
            tmp = cur_node.next
            cur_node.next = new_link
            new_link = cur_node
            cur_node = tmp
        return new_link


link = Nodes(1, Nodes(2, Nodes(3, Nodes(4, Nodes(5, Nodes(6, Nodes(7, Nodes(8, Nodes(9)))))))))
root = Nodes.reverse(link)
while root:
    print(root.val)
    root = root.next
