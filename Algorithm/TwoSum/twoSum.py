#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：twoSum.py
@Author  ：WL
@Date    ：2022/6/20 21:29 
@Describe: 两数之和
"""


def two_sum(lst: list, total: int) -> tuple:
    """
    列表中两数之和的下标
    :param lst: 列表
    :param total: 两数之后
    :return: 返回两数之和的下标
    """
    dt = {}
    for i in range(len(lst)):
        if total - lst[i] not in dt:
            dt[lst[i]] = i
        else:
            return dt[total - lst[i]], i


if __name__ == '__main__':
    data = [1, 4, 8, 9, 12, 45, 6, 8]
    num = 170
    res = two_sum(data, num)
    print(f"列表{data}中两数之和等于{num}的下标：{res}")
