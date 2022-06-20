#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：bulleSort02.py
@Author  ：WL
@Date    ：2022/6/20 14:29 
@Describe: 优化后的冒泡排序
"""


def bulle_sort(lst: list) -> list:
    """
    优化后的冒泡排序
    :param lst: 待排序列表
    :return: 排序后的列表
    """
    if len(lst) == 0:
        return lst

    count = 0
    # 排序多少躺
    for i in range(len(lst) - 1):
        count += 1
        # 每趟排序前加个标志位
        flag = False
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                flag = True

        print(f"第{i}轮排序：{lst}")
        if not flag:
            break

    return lst


if __name__ == '__main__':
    data = [3, 2, 8, 10, 45, 7, 6, 99, 100, 102]
    print(f"排序前：{data}")
    res = bulle_sort(data)
    print(f"排序后：{res}")
