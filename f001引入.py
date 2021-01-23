# coding=utf-8
# @Time : 2021/1/20/0020 上午 10:10
# @Author : Suger
# @File : f001引入.py
# @Software: PyCharm

"""
    a+b+c=1000  a^2 + b^2 = c^2
"""
import time


def meiju():
    # 枚举法
    # 时间复杂度 o^3
    start = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print(f"a:{a} b:{b} c:{c}")
    end = time.time()
    
    print(f"程序运行时间:{end - start}")


def meiju_2():
    # 枚举改进
    # 时间复杂度  o^2
    start = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c ** 2:
                print(f"a:{a} b:{b} c:{c}")
    end = time.time()
    
    print(f"程序运行时间:{end - start}")


if __name__ == '__main__':
    # 枚举法
    meiju_2()
