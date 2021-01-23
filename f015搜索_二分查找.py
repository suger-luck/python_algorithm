# coding=utf-8
# @Time : 2021/1/23/0023 上午 11:14 
# @Author : Suger
# @File : f015搜索_二分查找.py 
# @Software: PyCharm

"""
只能作用到顺序表上，并且是一个有序的表， 使用到下标
实现方法:
    递归
    非递归
最坏时间复杂度: O(logn)
最优时间复杂度: O(1)
"""


def binary_search(alist, item):
    """
    二分查找
    递归  -- 最容易理解
    :param alist:
    :param item:
    :return:
    """
    n = len(alist)
    if n > 0:
        # 折半
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    # 没有找到 返回 false
    return False


def binary_search_2(alist, item):
    """
    二分查找
    非递归
    :param alist:
    :param item:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            # 将最后一个下标改为前一部分最后一个的下标
            last = mid - 1
        else:
            # 将开头的下标改为后一部分第一个的下标
            first = mid + 1
    return False


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(li, 10))
    print(binary_search(li, 15))
    
    print(binary_search_2(li, 16))
    print(binary_search_2(li, 9))
