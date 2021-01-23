# coding=utf-8
# 两侧都可以取数据  相当于两个栈放一起
# @Time : 2021/1/21/0021 下午 14:35
# @Author : Suger
# @File : f008双端队列.py
# @Software: PyCharm

"""
Deque()  双端队列
add_front(item)  从队头添加一个Item
add_rear(item)  从队尾添加一个item
remove_front()  从队头取出一个元素
remove_rear()  从队尾取出一个元素
is_empty()  判空
size  个数
"""

class  Deque(object):
    """双端队列"""


    def __init__(self):
        self.__list = list()
    
    
    def add_front(self, item):
        """入队头部"""
        self.__list.insert(0,item)
        
    def add_rear(self, item):
        """入队尾部"""
        self.__list.append(item)
    
    def pop_front(self):
        """出队 从头部取元素"""
        return self.__list.pop(0)
        # return self.__list.pop()
    
    def pop_front(self):
        """出队 从尾部取元素"""
        return self.__list.pop()

    def is_empty(self):
        """判空"""
        return not self.__list
    
    
    def size(self):
        """个数"""
        return len(self.__list)


if __name__ == '__main__':
    dq = Deque()
 