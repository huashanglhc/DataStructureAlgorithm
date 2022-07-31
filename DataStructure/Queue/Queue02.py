#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：Queue02.py
@Author  ：WL
@Date    ：2022/7/31 16:07 
@Describe: 队列内置模块

双向队列： 两端都支持进队和出队操作
双向队列的基本操作：
    队首：进队/出队
    队尾：进队/出队
"""
from collections import deque

# 建立空队列
q = deque()
# 建立非空队列
# q = deque([100, 200, 300])
# 1. 队首进队，队尾出队
q.appendleft(2)
q.appendleft(3)
q.appendleft(4)
print(q.pop())
print(q.pop())

# 2. 队首出队，队尾进队
q.append(1)
print(q.popleft())


# 读取文件后10行
def tail(n):
    with open("file", "r", encoding="utf-8") as f:
        q1 = deque(f, n)
    return q1


for line in tail(5):
    print(line, end="")

