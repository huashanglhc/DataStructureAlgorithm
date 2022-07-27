#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DatasuctureAlgorithm 
@File    ：找出字符串中不重复的第一个字符.py
@Author  ：WL
@Date    ：2022/7/27 21:24 
@Describe: 找出一个字符串中第一次不重复出现的字符
"""


def search_str(s):
    dt = {}
    for i in range(len(s)):
        if s[i] not in dt:
            dt[s[i]] = 1
        else:
            dt[s[i]] += 1

    for i in range(len(s)):
        if dt[s[i]] == 1:
            return s[i], i + 1


if __name__ == '__main__':
    s = "adangdasgaadfgsdavdgsdad"
    print(search_str(s))



