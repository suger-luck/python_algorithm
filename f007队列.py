# coding=utf-8
# @Time : 2021/1/21/0021 上午 11:35
# @Author : Suger
# @File : f007队列.py
# @Software: PyCharm

"""
enqueue ： 入队
dequeue ： 出队
is_empty ： 判空
size : 个数
"""


class Queue(object):
    """队列"""
    
    def __init__(self):
        self.__list = list()
    
    def enqueue(self, item):
        """入队"""
        self.__list.append(item)
        # self.__list.insert(0,item)
    
    def dequeue(self):
        """出队 从头部取元素"""
        return self.__list.pop(0)
        # return self.__list.pop()
    
    def is_empty(self):
        """判空"""
        return  not self.__list
    
    def size(self):
        """个数"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())