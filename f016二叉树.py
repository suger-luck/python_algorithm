# coding=utf-8
# @Time : 2021/1/23/0023 下午 12:44 
# @Author : Suger
# @File : f016二叉树.py 
# @Software: PyCharm

"""
功能：
    添加
    遍历
        先序  根 左 右   根 -> 将左边的遍历完 - > 右
        中序 左 根 右
        后序 左 右 根
        广度优先 每一层 从左到右
"""

class Node(object):
    """节点类"""
    def __init__(self, elem):
        """存储数据结构"""
        self.elem = elem
        # 左节点
        self.lchild = None
        # 右节点
        self.rchild = None
        
class Tree(object):
    """二叉树"""
    def __init__(self):
        # 根节点
        self.root = None
    
    def add(self, item):
        """
        向完全二叉树的方向添加
        添加 item
        实现的方法采用的就是广度遍历 （层次遍历）
        :param item:
        :return:
        """
        
        node = Node(item)
        # 队列
        queue = list()
        queue.append(self.root)  # 添加根节点
        if self.root is None:
            # 如果根节点为空则直接将其作为根节点
            self.root = node
            return
        while queue:  # 队列不为空则进行寻找挂载节点
            cur_node = queue.pop(0)  # 读取一个节点
            if cur_node.lchild is None:
                # 判断左孩子是否为空，如果为空则添加，不为空则将其加到队列中
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                # 判断右孩子是否为空，如果为空则添加，不为空则将其加到队列中
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    
    
    def breadth_travel(self):
        """
        广度遍历 - 层次遍历
        父节点 -  左子树 - 右子树 - 左子树的左孩子 - 左子树的右孩子 - 右子树的左孩子 ........
        :return:
        """
        if self.root is None:
            return
        
        queue = [self.root]
        while queue:
            # 队列不为空的时候就遍历
            cur_node = queue.pop(0) # 取出节点
            print(cur_node.elem, end=" ")  # 打印节点数据
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)
        
    def preorder(self, node):
        """
        递归
        先序遍历
        根左右
        :param node:  根节点
        :return:
        """
        # 终止节点
        if node is None:
            # 当这个节点是none 时退出
            return
        # 打印节点  - 递归处理左子树  - 递归处理右子树
        print(node.elem, end=" ")
        self.preorder(node.lchild)  # 左子树
        self.preorder(node.rchild)  # 右子树
        
    def inorder(self, node):
        """
        递归
        中序遍历
        左根右
        :param node:  根节点
        :return:
        """
        # 终止节点
        if node is None:
            # 当这个节点是none 时退出
            return
        # 递归处理左子树 -  打印节点  - 递归处理右子树
        self.inorder(node.lchild)  # 左子树
        print(node.elem, end=" ")
        self.inorder(node.rchild)  # 右子树
    
    def postorder(self, node):
        """
        递归
        后序遍历
        左右根
        :param node:  根节点
        :return:
        """
        # 终止节点
        if node is None:
            # 当这个节点是none 时退出
            return
        # 递归处理左子树 - 递归处理右子树 -  打印节点
        self.postorder(node.lchild)  # 左子树
        self.inorder(node.rchild)  # 右子树
        print(node.elem, end=" ")

            
        
if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print("广度遍历/层次遍历:")
    tree.breadth_travel()  # 广度遍历
    print("先序遍历：")
    tree.preorder(tree.root)  # 先序遍历 传入 根节点
    print("中序遍历：")
    tree.inorder(tree.root)  # 中序遍历
    print("后序遍历：")
    tree.postorder(tree.root )  # 后序遍历
    