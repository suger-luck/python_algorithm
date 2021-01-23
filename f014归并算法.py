# coding=utf-8
# @Time : 2021/1/23/0023 上午 10:22 
# @Author : Suger
# @File : f014归并算法.py 
# @Software: PyCharm

"""
归并算法
递归拆分
最坏/最优时间复杂度：O(nlogn)
稳定性：稳定
空间上： 产生一段空间
"""


def merge_sort(alist):
    """
    归并算法
    递归拆分
    :param alist:
    :return:
    """
    n = len(alist)
    if n <= 1:
        # 当传入的列表中元素个数小于等于1时结束函数, 返回拆分后的元素
        return alist
    mid = n // 2
    
    #  left 与 right 返回的是 有序的子序列  递归调用自身
    left_list = merge_sort(alist[:mid])  # 前一部分拆分
    right_list = merge_sort(alist[mid:])  # 后一部分拆分
    
    # 将两个有序的子序列 合并成一个整体
    # merge(left_list, right_list)
    left_pointer, right_pointer = 0, 0  # 左侧列表与右侧列表的指针
    result = list()  # 合并之后的列表
    while left_pointer < len(left_list) and right_pointer < len(right_list):
        # 结束条件是 有一个指针走到头，即将左侧或者右侧列表中期中一个遍历完成之后退出循环   and ： 两个都为真则为真
        if left_list[left_pointer] <= right_list[right_pointer]:
            # 将小的或者相等的值添加到列表中
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    
    # 退出之后将期中一遍的列表进行向后追加
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]
    
    # 返回合并后的列表
    return result


if __name__ == '__main__':
    li = [1, 5, 6, 78, 5, 6, 1, 3, 1, 7]
    print(li)
    sorted_list = merge_sort(li)
    print(li)
    print(sorted_list)
