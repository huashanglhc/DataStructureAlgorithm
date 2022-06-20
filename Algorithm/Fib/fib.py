#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DataStructureAlgorithm 
@File    ：fib.py
@Author  ：WL
@Date    ：2022/6/20 18:21 
@Describe: 斐波拉契
"""


def fibonacci1(n: int) -> None:
    """
    斐波拉契
    :param n: 找前n个斐波拉契数列
    :return: None
    """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)


if __name__ == '__main__':
    fibonacci1(10)
