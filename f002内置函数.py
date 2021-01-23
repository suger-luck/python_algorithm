# coding=utf-8
# @Time : 2021/1/20/0020 上午 11:20
# @Author : Suger
# @File : f002内置函数.py
# @Software: PyCharm


from  timeit import Timer


# append  比insert 快

# 列表操作
# li = list()
# li.append()
# li.insert()


# 列表构造
# li = li1 + li2
# li = [i for i in range()]
# li list(range())
# li = list()  for i in range(): li.append(i)


def t1():
    li = list()
    for i in range(1000):
        li.append(i)


def t2():
    # 少使用可以使用  += 或者 extend()
    li = list()
    for i in range(1000):
        li = li + [i]

def t3():
    li = [i for i in range(1000)]
    
def t4():
    li = list(range(1000))
    
def t5():
    li = list()
    for i in range(1000):
        li.extend([i])

def t6():
    li = list()
    for i in range(1000):
        li.insert(0,i)

def main():
    time1 = Timer("t1()", "from __main__ import t1")
    print(f"列表append:{time1.timeit(1000)}")
    time2 = Timer("t2()", "from __main__ import t2")
    print(f"列表加法:{time2.timeit(1000)}")
    time3 = Timer("t3()", "from __main__ import t3")
    print(f"列表生成器:{time3.timeit(1000)}")
    time4 = Timer("t4()", "from __main__ import t4")
    print(f"list(range()):{time4.timeit(1000)}")
    time5 = Timer("t5()", "from __main__ import t5")
    print(f"extend:{time5.timeit(1000)}")
    time6 = Timer("t6()", "from __main__ import t6")
    print(f"insert:{time6.timeit(1000)}")
    
    
if __name__ == '__main__':
    main()