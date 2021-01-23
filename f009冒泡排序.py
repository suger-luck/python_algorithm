# coding=utf#
# @Time : 2021/1/22/0022 上午 09:30
# @Author : Suger
# @File : f009冒泡排序.py
# @Software: PyCharm

"""
冒泡排序
最坏时间复杂度  O(n^2)
改进后  最优时间复杂度 O(n)
稳定性 : 稳定
"""

def bubble_sort(alist):
    """
        冒泡排序 -- 顺序表
        从内层循环写到外层循环
        最坏时间复杂度  O(n^2)
        稳定性 : 稳定
    """
    n = len(alist)
    for j in range(n-1):
        # [0,1,2,3,4,....,n-2]
        # 记录次数
        for i in range(0,n-j-1):
            # [n-1,n-2,n-3,.....,1]   每一次的最大值
            # 从头到尾遍历
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

def bubble_sort_2(alist):
    """
        冒泡排序 -- 顺序表
        从内层循环写到外层循环
    """
    n = len(alist)
    for j in range(n-1,0,-1):
        # [n-1,n-2,n-3,...,1]
        # 记录次数
        for i in range(j):
            # 从头到尾遍历
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

def bubble_sort_cut(alist):
    """
        冒泡排序 -- 顺序表
        从内层循环写到外层循环
        改进  最优时间复杂度 O(n)
    """
    n = len(alist)
    for j in range(n-1):
        # 记录次数
        count = 0
        for i in range(0,n-j-1):
            # 从头到尾遍历
            if alist[i] > alist[i+1]:
                count+=1
                alist[i], alist[i+1] = alist[i+1], alist[i]
                
        if not count:
            # print("退出")
            return


if __name__ == '__main__':
    li = [1, 5, 6, 78, 5, 6, 1, 3, 1, 7]
    li_cut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(li)
    print(li_cut)
    bubble_sort(li)
    bubble_sort_2(li)
    bubble_sort_cut(li_cut)
    print(li)
    print(li_cut)
