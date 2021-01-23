# coding=utf-8
# @Time : 2021/1/20/0020 下午 14:35
# @Author : Suger
# @File : f004双向链表.py
# @Software: PyCharm

"""
第一个节点为    头结点
最后一个节点为 尾结点
实现一下功能：
是否为空            is_empty()
链表长度            length()
遍历整个列表        travel()
链表头部添加元素    add(item)   O(1)
链表尾部添加元素    append(item)  O(n)
指定位置添加元素    insert(pos,item)  O(n)
删除节点            remove(item)
查找节点是否存在    search(item)   O(n)
"""

from f003单向链表 import SingleNodeList

class Node(object):
    """双向链表的节点"""
    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None
        

class DoubleLinkList(SingleNodeList):
    """实现双链表， 继承单链表的东西"""
    def __init__(self):
        self.__head = None

    # def is_empty(self):
    #     """判断是否为空"""
    #     return self.__head is None  # 有则为False 没有则为True
    #
    # def length(self):
    #     """返回链表的长度"""
    #     # 两种记录方式
    #     # 1. 最初计数为0 --> 判断cur== None 退出循环    比较好
    #     # 2. 最初计数为1 --> 判断cur.next == None 退出循环   1） 头结点为None的时候
    #     cur = self.__head  # 游标  用来移动遍历节点
    #     count = 0  # 记录个数
    #     while cur != None:  # 当游标的next 等于None时退出
    #         count += 1
    #         cur = cur.next  # 往后移动
    #
    #     return count
    #
    # def travel(self):
    #     """遍历整个链表"""
    #     cur = self.__head
    #     while cur != None:
    #         print(cur.elem, end=" ")
    #         cur = cur.next
    #     print("\n")

    def add(self, item):
        """在头部添加元素， 头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """在尾部添加元素, 尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos:  从0开始索引
        :param item: 节点
        :return:
        """
        cur = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除某个元素 删除第一个元素"""
        # 两种方法  1. 两个游标pre.next = cur.next  2. 一个游标   pre.next = pre.next.next
        # 两个游标
        cur = self.__head
        while cur != None:
            if cur.elem != item:
                cur = cur.next
            else:
                # 先判断此节点是否是头结点，头结点的话，直接使用self.__head指向下一个节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                break
    
    # def search(self, item):
    #     """查找节点是否存在"""
    #     cur = self.__head
    #     while cur != None:
    #         if cur.elem == item:
    #             return True
    #         else:
    #             cur = cur.next
    #     return False

if __name__ == '__main__':
    ddll = DoubleLinkList()
    dll = SingleNodeList()
    print(f"是否为空：{dll.is_empty()}")
    print(f"个数:{dll.length()}")

    dll.append(1)
    print(f"是否为空：{dll.is_empty()}")
    print(f"个数:{dll.length()}")

    dll.append(6)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)

    print(f"个数:{dll.length()}")
    print("遍历：")
    dll.travel()

    dll.add(789)
    print("遍历：")
    dll.travel()

    print("指定位置插入遍历:")
    dll.insert(-1, 456)
    dll.travel()
    dll.insert(3, 46)
    dll.travel()
    dll.insert(10, 56)
    dll.travel()

    print("删除元素遍历：")
    dll.remove(789)
    dll.travel()
    dll.remove(56)
    dll.travel()