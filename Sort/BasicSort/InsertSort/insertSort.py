#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：insertSort.py
@Author  ：WL
@Date    ：2022/6/20 15:37 
@Describe: 插入排序
"""


def insert_sort(lst: list) -> list:
    """
    插入排序
    :param lst: 待排序列表
    :return: 排序后列表
    """
    if len(lst) <= 1:
        return lst

    # 无序区循环次数
    for i in range(1, len(lst)):
        # 摸到的牌
        tmp = lst[i]
        # 手里牌下标
        j = i - 1
        while j >= 0 and lst[j] > tmp:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = tmp

    return lst


if __name__ == '__main__':
    data = [3, 2, 8, 10, 45, 7, 6, 99, 100, 102]
    print(f"排序前：{data}")
    res = insert_sort(data)
    print(f"排序后：{res}")
