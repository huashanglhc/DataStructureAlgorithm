#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：selectSort.py
@Author  ：WL
@Date    ：2022/6/20 15:10 
@Describe: 选择排序
"""
import random


def select_sort(li: list) -> list:
    for i in range(len(li) - 1):
        min_loc = i
        # 每轮比较更新最小元素位置
        for j in range(i + 1, len(li)):
            if li[j] <= li[min_loc]:
                min_loc = j
        print(f"第{i}轮排序结果：{li}")
        # 每轮循环后交换第i位置上元素和最小元素位置
        li[i], li[min_loc] = li[min_loc], li[i]
    return li


if __name__ == '__main__':
    # lst = [random.randint(10, 1000) for _ in range(100)]
    lst = [1, 5, 136, 138, 77, 6, 9, 10, 11, 12, 13, 14, 16]
    print(f"排序前列表：{lst}")
    res = select_sort(lst)
    print(f"排序后列表：{res}")
