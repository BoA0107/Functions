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
            pass
        elif num == '3':
            pass
        elif num.lower() == 'q':
            sys.exit()
        else:
            num = input('\t\t\t\t输入错误，请重新输入：')


def info_f():
    while True:
        print('基金代码\t\t', '基金名称\t\t', '昨日净值\t', '今日估值\t', '今日涨幅')
        print('-' * 60)
        for c in codes:
            get_f(c)
        print('-' * 60)
        x = input("\t\t\t输入h返回首页，其他键重新查询：")
        if x.lower() == 'h':
            show()
        elif x.lower() == 'q':
            sys.exit()


def get_f(code):
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
    pass

def add_do():
    pass


def del_f():
    pass


def save_f():
    pass


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
