#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import random
import operator
import argparse
from fractions import Fraction

def get_Parameter():#命令行控制模块
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help='设定题目数量',type=int)
    parser.add_argument('-r', help='设定数值范围',type=int)
    return parser.parse_args()

class com(object):
    def __init__(self, r):#初始化
        self.r=r

    def get_Arithmeticl(self):#获得随机数字与符号
        symbol=[]
        numerical=[]
        syb=0
        n=1
        m=0
        i=random.randint(1, 3)
        for x in range(i):
            sy=random.choice(['+','-','×','÷'])
            if sy=='+'or sy=='-':
                syb +=10**(i-x-1)
            else :
                syb += 2 * (10 ** (i - x - 1))
            symbol.append(sy)
        if self.r < 10:
            n = int(10 / self.r)
        if n==1:
            while m <= i:
                numerical.append(Fraction(random.randint(1, self.r), random.randint(1, self.r)))
                m+=1
        else:
            while m <= i:
                nu = Fraction(random.randint(1, self.r * n), random.randint(1, self.r * n))
                if nu<=self.r:
                    numerical.append(nu)
                    m += 1
        return symbol,syb,numerical,i

def get_Calculate(a,b,c):#四则运算
    if c=='+':
        results=a+b
    elif c=='-':
        results=a-b
    elif c=='×':
        results=a*b
    else:results=a/b
    return results

def get_Conversion(fraction):#假分数转化真分数
    if fraction.numerator%fraction.denominator==0:
        return '%d'%(fraction.numerator/fraction.denominator)
    elif fraction.numerator>fraction.denominator:
        a=int(fraction.numerator/fraction.denominator)
        b, c = fraction.numerator - a * fraction.denominator, fraction.denominator
        return '%d%s%d%s%d' % (a,'’',b,'/',c)
    else:
        b, c = fraction.numerator, fraction.denominator
        return '%d%s%d' % (b,'/',c)

def set_Formula(symbol,numerical,syb):#算术表达式
    s=''
    if syb>100:
        if syb == 112 or syb ==212:
            s = '(%s %s %s %s %s) %s %s = ' % (get_Conversion(numerical[0]), symbol[0],
            get_Conversion(numerical[1]),symbol[1], get_Conversion(numerical[2]), symbol[2], get_Conversion(numerical[3]))
        elif syb == 121 or syb ==122:
            s = '(%s %s %s) %s %s %s %s = ' % (get_Conversion(numerical[0]), symbol[0],
            get_Conversion(numerical[1]),symbol[1], get_Conversion(numerical[2]), symbol[2], get_Conversion(numerical[3]))
        else:
            s = '%s %s %s %s %s %s %s = ' % (get_Conversion(numerical[0]), symbol[0],
            get_Conversion(numerical[1]),symbol[1], get_Conversion(numerical[2]), symbol[2], get_Conversion(numerical[3]))
    elif syb>10:
        if syb == 12:
            s = '(%s %s %s)%s %s = ' % (get_Conversion(numerical[0]), symbol[0],
            get_Conversion(numerical[1]), symbol[1], get_Conversion(numerical[2]))
        else:
            s = '%s %s %s %s %s = ' % (get_Conversion(numerical[0]), symbol[0],
            get_Conversion(numerical[1]), symbol[1], get_Conversion(numerical[2]))
    else :
        s ='%s %s %s = ' % (get_Conversion(numerical[0]),symbol[0],get_Conversion(numerical[1]))
    return s

def get_Formula(n,r):#生成题目和答案列表
    Exercises,Answers,Exercises1,Exercises2=[],[],[],[]
    x=1
    while x<n+1:
        symbol, syb, numerical,i = com(r).get_Arithmeticl()
        results = numerical[0]
        judge = True
        for y in range(i):
            calculate=get_Calculate(results,numerical[y+1],symbol[y])
            if calculate>=0:#判断算式是否合法
                answer=calculate
            else:
                judge=False
                break
        if judge:#查重
            try:
                num=Answers.index(answer)#第一个重复答案的索引
                if operator.eq(Exercises1[num],symbol) and operator.eq(Exercises2[num],numerical):
                    pass
            except ValueError as e:#可以写入
                Answers.append(answer)
                Exercises1.append(symbol)
                Exercises2.append(numerical)
                Exercises.append('%d. %s'%(x,set_Formula(symbol,numerical,syb)))
                x+=1
        else:pass
    return Exercises,Answers

def text_save(filename, data):#filename为写入文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    file.seek(0)
    file.truncate() # 清空文件
    for x in data:
        x='%s\n'%(x)
        file.write(x)
    file.close()
    print('%s文件保存成功'%filename)

def main():
    args = get_Parameter()
    if args.n:
        n = args.n
    if args.r:
        r = args.r
        Exercises, Answers = get_Formula(n, r)
        for x in range(n):
            Answers[x] = '%d. %s' % (x + 1, get_Conversion(Answers[x]))
        print('本次共生成题目%d道\n题目数值范围为0-%d' % (n, r))
        text_save('Exercises.txt', Exercises)
        text_save('Answers.txt', Answers)

if __name__ == '__main__':
    main()