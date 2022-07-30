#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：stack.py
@Author  ：WL
@Date    ：2022/7/26 22:31 
@Describe: 栈的实现

栈： 栈（Stack），一种线性数据结构，它的特点在于只能允许容器的一端（称为栈顶端）进行插入数据和删除数据的运算。
栈顶：允许删除和插入的一端称为栈顶
栈低：与栈顶相对的一端称为栈底
栈的线性表分类：顺序栈和链式栈
顺序栈：即堆栈的顺序存储结构。利用一组地址连续的存储单元存放自栈低到栈顶的元素，同时使用指针top指示栈顶元素在顺序栈中的位置
链式栈：即堆栈链式存储结构。利用单链表的方式来实现堆栈。栈中元素按照插入顺序依次插入到链表的第一个节点之前，并使用栈顶top指示
        栈顶元素，top永远指向的头节点位置。

栈的实现方式1： 顺序栈（列表实现）
"""


class Stack:
    def __init__(self, size=100):
        self.stack = []
        self.size = size
        self.top = -1

    def is_empty(self):
        """判断栈是否空"""
        return self.top == -1

    def is_full(self):
        """判断栈是否满"""
        return self.top + 1 == self.size

    def push(self, value):
        """入栈"""
        if self.is_full():
            raise ValueError("Stack is full....")

        self.top += 1
        self.stack.append(value)

    def pop(self):
        """出栈"""
        if self.is_empty():
            raise ValueError("stack is empty...")

        self.top -= 1
        return self.stack.pop()

    def get_top(self):
        """获取栈顶元素"""
        if self.is_empty():
            raise ValueError("stack is empty...")

        return self.stack[self.top]


if __name__ == '__main__':
    s = Stack(5)
    print("判断栈是否为空：", s.is_empty())
    print("判断栈是否满：", s.is_full())
    for i in range(4):
        s.push(i + 1)
    print("获取栈顶元素：", s.get_top())
    print("栈中加入元素：", s.push(100))
    print("判断栈是否满：", s.is_full())
    for i in range(5):
        print("出栈：", s.pop())
