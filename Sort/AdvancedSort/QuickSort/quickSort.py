#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：quickSort.py
@Author  ：WL
@Date    ：2022/6/20 16:09 
@Describe: 快速排序
"""


def place(lst: list, left: int, right: int) -> int:
    """
    找到一个元素，使得列表中所有比这个元素小的元素排到左边，比它小的全部都排在它右边
    :param right: 列表右边位置
    :param left: 列表左边起始位置
    :param lst: 待归位元素
    :return: 归位元素的位置
    """
    tmp = lst[left]
    while left < right:
        # 从右边找比tmp小的元素
        while left < right and lst[right] >= tmp:
            right -= 1
        # 把右边的值放到左边的空位上
        lst[left] = lst[right]
        # 从左边找比tmp大的元素
        while left < right and lst[left] <= tmp:
            left += 1
        # 把左边的值放到右边的空位上
        lst[right] = lst[left]

    lst[left] = tmp
    return left


def quick_sort(lst: list, left: int, right: int) -> list:
    """
    快速排序
    :param right: 列表右边位置
    :param left: 列表左边起始位置
    :param lst: 待排序列表
    :return: 排序后列表
    """
    if left < right:
        mid = place(lst, left, right)
        quick_sort(lst, left, mid)
        quick_sort(lst, mid + 1, right)
    return lst


if __name__ == '__main__':
    data = [3, 2, 8, 10, 45, 7, 6, 99, 100, 102]
    print(f"排序前：{data}")
    res = quick_sort(data, 0, len(data) - 1)
    print(f"排序后：{res}")
