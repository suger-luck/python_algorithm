# coding=utf-8
# @Time : 2021/1/20/0020 下午 14:05
# @Author : Suger
# @File : f003单向链表.py
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
# 顺序表 ： 优点：访问元素的时间复杂度为O(1)， 内存是一块连续的内存
# 链表 ： 优点： 内存不需要是连续的内存， 访问元素的时间复杂度为O(n), 不足： 消耗空间较大

class Node(object):
    """节点"""
    
    def __init__(self, elem):
        """
            初始节点类
            数据和下一个节点的地址
        """
        self.elem = elem
        self.next = None


class SingleNodeList(object):
    """单链表的节点结构"""
    
    def __init__(self, node=None):
        self.__head = node
    
    def is_empty(self):
        """判断是否为空"""
        return self.__head is None  # 有则为False 没有则为True
    
    def length(self):
        """返回链表的长度"""
        # 两种记录方式
        # 1. 最初计数为0 --> 判断cur== None 退出循环    比较好
        # 2. 最初计数为1 --> 判断cur.next == None 退出循环   1） 头结点为None的时候
        cur = self.__head  # 游标  用来移动遍历节点
        count = 0  # 记录个数
        while cur != None:  # 当游标的next 等于None时退出
            count += 1
            cur = cur.next  # 往后移动
        
        return count
    
    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("\n")
    
    def add(self, item):
        """在头部添加元素， 头插法"""
        # 方法一
        # cur = self.__head
        # node = Node(item)
        # self.__head = node
        # node.next = cur
        
        # 方法二
        node = Node(item)
        node.next = self.__head
        self.__head = node
    
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
    
    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos:  从0开始索引
        :param item: 节点
        :return:
        """
        pre = self.__head
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            count = 0
            while (count + 1) < pos:
                count += 1
                pre = pre.next
            node = Node(item)
            node.next = pre.next
            pre.next = node
    
    def remove(self, item):
        """删除某个元素 删除第一个元素"""
        # 两种方法  1. 两个游标pre.next = cur.next  2. 一个游标   pre.next = pre.next.next
        # 两个游标
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem != item:
                pre = cur
                cur = cur.next
            else:
                # 先判断此节点是否是头结点，头结点的话，直接使用self.__head指向下一个节点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
        
        # 单个游标
        # if self.__head !=None:
        #     if self.__head.elem == item:
        #         self.__head =self.__head.next
        #     else:
        #         pre = self.__head
        #         while pre.next != None:
        #             if pre.next.elem == item:
        #                 pre.next = pre.next.next
        #                 break
        #             pre = pre.next
    
    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    ll = SingleNodeList()
    print(f"是否为空：{ll.is_empty()}")
    print(f"个数:{ll.length()}")
    
    ll.append(1)
    print(f"是否为空：{ll.is_empty()}")
    print(f"个数:{ll.length()}")
    
    ll.append(6)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    
    print(f"个数:{ll.length()}")
    print("遍历：")
    ll.travel()
    
    ll.add(789)
    print("遍历：")
    ll.travel()
    
    print("指定位置插入遍历:")
    ll.insert(-1, 456)
    ll.travel()
    ll.insert(3, 46)
    ll.travel()
    ll.insert(10, 56)
    ll.travel()
    
    print("删除元素遍历：")
    ll.remove(789)
    ll.travel()
    ll.remove(56)
    ll.travel()
