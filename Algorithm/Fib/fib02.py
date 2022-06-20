#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：fib02.py
@Author  ：WL
@Date    ：2022/6/20 18:25 
@Describe: 
"""


def fibonacci2(n: int):
    """
    斐波拉契
    :param n: 找前n个斐波拉契数列
    :return: None
    """
    if n < 2:
        return 1
    else:
        return fibonacci2(n - 1) + fibonacci2(n - 2)


if __name__ == '__main__':
    for i in range(10):
        print(fibonacci2(i))
