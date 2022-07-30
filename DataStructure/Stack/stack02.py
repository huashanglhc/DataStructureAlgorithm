#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：stack02.py
@Author  ：WL
@Date    ：2022/7/30 16:32 
@Describe: 链式栈

栈的应用：
    1. 使用栈可以很方便的保存和取用信息，因此长被用作算法和程序中的辅助结构，临时保存信息，供后面操作中使用。
        例如： 操作系统中的函数调用栈，浏览器中的前进、后退功能
    2. 堆栈的后进先出的规则，可以保证特定的存取顺序
        例如：翻转一组元素顺序、铁路列车车辆调度
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, val):
        """入栈"""
        cur = Node(val)
        cur.next = self.top
        self.top = cur

    def pop(self):
        """出栈"""
        if self.is_empty():
            raise ValueError("stack is empty....")
        cur = self.top
        self.top = self.top.next
        print("出栈：", cur.val)
        del cur

    def get_top(self):
        """获取栈顶元素"""
        if self.is_empty():
            raise ValueError("stack is empty....")
        return self.top.val


if __name__ == '__main__':
    s = Stack()
    print("判断栈是否为空：", s.is_empty())
    for i in range(4):
        s.push(i + 1)
    print("获取栈顶元素：", s.get_top())
    for i in range(3):
        s.pop()
    print("获取栈顶元素：", s.get_top())
