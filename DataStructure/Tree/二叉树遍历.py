#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：二叉树遍历.py
@Author  ：WL
@Date    ：2022/7/27 21:19 
@Describe: 二叉树遍历
前序遍历：根-左-右
中序遍历：左-根-右
后序遍历：左-右-根

"""
from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

root = e


def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)


def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)


def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")


def level_order(root):
    queue = deque()
    queue.append(root)
    # 只要队不空
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


print("前序遍历-------------->")
pre_order(root)
print()
print("中序遍历-------------->")
in_order(root)
print()
print("后序遍历-------------->")
post_order(root)
print()
print("层次遍历-------------->")
level_order(root)
