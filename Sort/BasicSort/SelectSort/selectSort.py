#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：selectSort.py
@Author  ：WL
@Date    ：2022/6/20 15:10 
@Describe: 选择排序
"""


def select_sort(lst: list) -> list:
    """
    选择排序
    :param lst: 待排序列表
    :return: 排序后列表
    """
    if len(lst) <= 1:
        return lst

    for i in range(len(lst) - 1):
        min_loc = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_loc]:
                min_loc = j

        lst[i], lst[min_loc] = lst[min_loc], lst[i]

    return lst


if __name__ == '__main__':
    data = [4, 9, 2, 3, 10, 45, 32, 65, 89, 76, 99, 66]
    print(f"排序前：{data}")
    res = select_sort(data)
    print(f"排序后：{res}")
