#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：bubbleSort.py
@Author  ：WL
@Date    ：2022/6/20 11:58 
@Describe: 冒泡排序
"""


def bulle_sort(lst: list) -> list:
    """
    冒泡排序
    :param lst: 待排序列表
    :return: 排序后的列表
    """
    if len(lst) == 0:
        return lst

    # 循环多少轮
    for i in range(len(lst) - 1):
        # 每轮无序区元素长度再减少
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]

    return lst


if __name__ == '__main__':
    data = [7, 2, 9, 18, 38, 5, 87, 46]
    print(f"排序前：{data}")
    res = bulle_sort(data)
    print(f"排序后：{res}")
