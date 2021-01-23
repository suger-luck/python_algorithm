# coding=utf-8
# @Time : 2021/1/22/0022 上午 11:05
# @Author : Suger
# @File : f011插入排序.py
# @Software: PyCharm

"""
插入排序
时间复杂度 ： O(n^2)
优化后的时间复杂度 : O(n)
稳定性 : 稳定
"""

def insert_sort(alist):
    """
    插入算法
    :param alist:
    :return:
    """
    n = len(alist)
    for i in range(1, n):
        # 从右边的无序序列中取出多少个元素
        for j in range(i, 0, -1):
            # 从后往前比较  从后边取出元素进行与前面的一个元素比较，如果小则交换
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:
                # 进行优化
                break


def insert_sort_2(alist):
    """
    插入算法
    while循环
    :param alist:
    :return:
    """
    n = len(alist)
    for j in range(1, n):
        i = j
        while i > 0:
            # 因为在排序的郭晨中左边序列中的值是依次增大的，如果当前值不小于比较的值，就说明这个值比前面的值都大，所以退出
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                # 如果没有break的话就会一直循环到0，这一步作为的是优化的操作
                break


if __name__ == '__main__':
    li = [1, 5, 6, 78, 5, 6, 1, 3, 1, 7]
    print(li)
    insert_sort(li)
    print(li)
