#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：Queue.py
@Author  ：WL
@Date    ：2022/7/31 15:42 
@Describe: 队列实现
"""


class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0
        self.front = 0

    def is_empty(self):
        """判断队列是否为空"""
        return self.rear == self.front

    def is_full(self):
        """判断队列是否满"""
        return self.front == (self.rear + 1) % self.size

    def push(self, val):
        """队列中添加元素"""
        if not self.is_full():
            # self.queue.insert(0, val)
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = val

    def pop(self):
        """队列中弹出元素"""
        if not self.is_empty():
            # self.queue.pop()
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]

    def traverse(self):
        """遍历队列"""
        if not self.is_empty():
            for _ in range(self.size - 1):
                print("队列中弹出元素：", self.pop())


if __name__ == '__main__':
    q = Queue(6)
    print("判断队列是否满：", q.is_full())
    for i in range(6):
        print("入队元素：", i + 1)
        q.push(i + 1)
    print("判断队列是否满：", q.is_full())
    q.traverse()
    print("判断队列是否为空：", q.is_empty())
