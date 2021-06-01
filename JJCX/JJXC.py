# -*- coding:utf-8 -*-
import sys
import requests


def show():
    print('\t\t\t基金查询')
    print('-' * 40)
    print('\t\t\t1. 基金查询')
    print('\t\t\t2. 基金添加')
    print('\t\t\t3. 基金删除')
    print('\t\t\tq. 退出系统')
    print('-' * 40)
    num = input('\t\t\t输入编号：')

    while True:
        if num == '1':
            pass
        elif num == '2':
            pass
        elif num == '3':
            pass
        elif num.lower() == 'q':
            sys.exit()
        else:
            num = input('\t\t\t输入错误，请重新输入：')


def info_f():
    for c in codes:
        get_f(c)


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
        print ("{0:10} {1:10} {2:10} {3:10} {4:10}".format(dct['fundcode'], dct['name'][:6], dct['dwjz'], dct['gsz'],
                                         dct['gszzl']))


def add_f():
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

    # show()

    info_f()
