# coding=utf-8
# @Time : 2021/1/22/0022 下午 14:30
# @Author : Suger
# @File : f013快速排序.py
# @Software: PyCharm

"""
快速排序
在递归的时候即使分为两个部分，也要对原来的列表进行操作
最优时间复杂度   O(nlogn)  以2为底
最坏时间复杂度  O(n^2)
稳定性 : 不稳定
"""

def quick_sort(alist, first, last):
    """
    快速排序
    在递归的时候即使分为两个部分，也要对原来的列表进行操作
    最优时间复杂度   O(nlogn)  以2为底
    最坏时间复杂度  O(n^2)
    稳定性 : 不稳定
    :param alist:
    :return:
    """
    if first >= last:
        # 列表中只有一个元素的时候，直接终止程序运行
        return
    
    # 取出的值
    mid_value = alist[first]
    # 左侧标记
    low = first
    # 右侧标记
    high = last
    
    # 对某一个元素进行快速排序
    while low < high:
        while low < high and alist[high] >= mid_value:
            # 左侧的标记与右侧标记没有重合 并且 右侧的值比取出的值大，则进行将右侧的标记向左移动
            high -= 1
        
        # 当上述条件不符合的时候 将左侧值与右侧值换位置
        alist[low] = alist[high]
        
        while low < high and alist[low] < mid_value:
            # 左侧标记向右移动
            low += 1
        
        # 当上数条件不符的时候 互换位置
        alist[high] = alist[low]
    
    alist[low] = mid_value
    
    # 递归
    # 对左边的列表进行排序
    quick_sort(alist, first, low - 1)
    # 对右边的列表进行排序
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    li = [1, 5, 6, 78, 5, 6, 1, 3, 1, 7]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
