#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：binarySearch.py
@Author  ：WL
@Date    ：2022/6/20 11:37 
@Describe:  二分查找
"""


def binary_search(lst: list, element: int) -> int:
    """
    二分查找
    :param element: 待查找的元素
    :param lst: 待查找的元素列表
    :return: 查找元素小标
    """
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        # 查找元素比中间元素小
        if lst[mid] < element:
            left = mid + 1
        elif lst[mid] > element:
            right = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    data = [1, 3, 5, 8, 17, 20, 25, 35, 90, 102]
    ele = 123
    res = binary_search(data, ele)
    print(f"{ele}在列表{data}中的下标：{res}")
