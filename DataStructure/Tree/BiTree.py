#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：BiTree.py
@Author  ：WL
@Date    ：2022/7/27 16:25 
@Describe: 二叉树定义
"""


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
print(root.lchild.rchild.data)
