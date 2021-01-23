# coding=utf-8
# @Time : 2021/1/21/0021 上午 09:30
# @Author : Suger
# @File : f006栈.py
# @Software: PyCharm


# 使用线性表   list


#  使用线性制作栈的话 压栈和出栈使用在尾部进行数据操作
#  使用链表在做栈的话 压栈和出栈使用在头部进行操作
# 原因： 时间复杂度为O(1)

# 逻辑中假的：  "" 0 {} () []

"""
实现功能
压栈 push
出栈 pop  栈顶弹出元素

Stack()  创建一个空的栈
push(item)  添加一个新元素到栈顶
pop()  弹出栈顶元素
peek()  返回栈顶元素
is_empty()  判断栈是否为空
size()  返回栈的元素个数
"""


class Stack(object):
    """栈：使用列表完成"""
    
    def __init__(self):
        """构造容器"""
        self.__list = list()
    
    def push(self, item):
        """压栈"""
        self.__list.append(item)
        
        # 在头部
        # self.__list.insert(0,item)
    
    def pop(self):
        """出栈"""
        return self.__list.pop()
        
        # 在头部
        # self.__list.pop(0)
    
    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
    
    def is_empty(self):
        """判空"""
        # return self.__list is []
        return  not self.__list
    def size(self):
        """元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    
    
    
