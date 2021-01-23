# coding=utf-8
# @Time : 2021/1/22/0022 下午 13:30
# @Author : Suger
# @File : f012希尔排序.py
# @Software: PyCharm

"""
希尔排序
时间复杂度 :O(n^2)
最优的时间复杂度为  : O(n^1.3)
稳定性 ： 不稳定
"""


def shell_sort(alist):
    """
    希尔排序
    :param alist:
    :return:
    """

    n = len(alist)
    gap = n // 2  # 步长  取元素的一般
    while gap >= 1:
        # gap 变化到0之前，gap的变化
        # 插入算法与普通的插入算法的区别就是步长
        for  j in range(gap,n):
            # [gap,gap+1,gap+2,gap+2]
            i = j
            while i >0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break
        # gap 缩短  步长
        gap //= 2


if __name__ == '__main__':
    li = [1, 5, 6, 78, 5, 6, 1, 3, 1, 7]
    print(li)
    shell_sort(li)
    print(li)


