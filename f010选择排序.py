# coding=utf-8
# @Time : 2021/1/22/0022 上午 10:10
# @Author : Suger
# @File : f010选择排序.py
# @Software: PyCharm

"""
选择排序
时间复杂度为 O(n^2)
稳定性 ：  不稳定
"""


def select_sort(alist):
    """
    选择排序
    先写内部的程序在写外部的程序
    时间复杂度为 O(n^2)
    稳定性 ：  不稳定
    :param alist:
    :return:
    """
    n = len(alist)
    for j in range(n - 1):
        # [0,1,2,3,...,n-2]
        min_index = j
        for i in range(j + 1, n):
            if alist[i] < alist[min_index]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
    li = [1, 5, 6, 78, 5, 6, 1, 3, 1, 7]
    print(li)
    select_sort(li)
    print(li)
