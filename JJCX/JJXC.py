# -*- coding:utf-8 -*-
import sys
import requests


def show():
    print('\t\t\t\t基金查询')
    print('-' * 60)
    print('\t\t\t\t1. 基金查询')
    print('\t\t\t\t2. 基金添加')
    print('\t\t\t\t3. 基金删除')
    print('\t\t\t\tq. 退出系统')
    print('-' * 60)
    print()
    num = input('\t\t\t\t输入编号：')
    print()
    print('-' * 60)

    while True:
        if num == '1':
            info_f()
        elif num == '2':
            add_f()
        elif num == '3':
            del_f()
        elif num.lower() == 'q':
            sys.exit()
        else:
            num = input('\t\t\t\t输入错误，请重新输入：')


def info_f():
    while True:
        print('基金代码\t\t', '基金名称\t\t', '昨日净值\t', '今日估值\t', '今日涨幅')
        print('-' * 60)
        for c in codes:
            do_info(c)
        print('-' * 60)
        x = input("\t\t\t输入h返回首页，其他键重新查询：")
        if x.lower() == 'h':
            show()
        elif x.lower() == 'q':
            sys.exit()


def do_info(code):
    url = u + code + '.js'
    req = requests.get(url)
    if req.status_code == 200:
        dct = {}
        info = req.text.strip('jsonpgz({});')
        info = info.split(',')[:6]
        for i in info:
            x, y = i.split(':')
            dct[x.strip('"')] = y.strip('"')
        print("{0}\t\t {1:6}\t\t {2}\t\t {3}\t\t {4}\t\t".format(dct['fundcode'], dct['name'][:6], dct['dwjz'],
                                                                 dct['gsz'],
                                                                 dct['gszzl']))


def add_f():
    code = input("\t\t\t\t输入代码或h：")
    while True:
        if code.lower() == 'h':
            show()
        elif code.lower() == 'q':
            sys.exit()
        elif code in codes:
            code = input('\t\t\t\t代码已存在，输入新代码或h返回首页：')
        else:
            x = check_code(code)
            if x == False:
                code = input('\t\t\t\t输入不正确，输入新代码或h返回首页：')
            else:
                codes.append(code)
                with open(filename, 'a') as file:
                    file.write(code + '\n')
                code = input('\t\t\t\t保存成功，继续添加或h返回首页：')


def del_f():
    while True:
        if len(codes) == 0:
            print("当前无基金代码保存。")
            show()
        else:
            print("现存基金数目：" + str(len(codes)))
            for i in range(len(codes)):
                print(i + 1, codes[i])
            x = input("输入要删除的序号或h返回首页：")
            if x.lower()=='h':
                show()
            elif x.lower()=='q':
                sys.exit()
            elif type(int(x))==False:
                print('aa')


def check_code(num):
    try:
        if type(int(num)) == int:
            if len(num) == 6:
                url = u + num + '.js'
                req = requests.get(url)
                if req.status_code == 200:
                    return True
                else:
                    return False
            else:
                return False
    except:
        return False


def open_file():
    codes = []
    try:
        file = open(filename, 'r')
        c = file.readlines()
        for x in c:
            codes.append(x.strip('\n'))
        file.close()
        return codes
    except:
        file = open(filename, 'w')
        file.close()
        codes = []
        return codes


if __name__ == "__main__":
    u = r'http://fundgz.1234567.com.cn/js/'
    filename = r'code.txt'
    codes = open_file()

    show()
