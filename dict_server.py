from socket import *
import os
import time
import signal
import pymysql
import sys

# 定义需要的全局变量
DICT_TEXT = './dict.txt'
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

#　流程控制
def main():
    # 创建数据库连接
    db = pymysql.connect('localhost','root','123456','dict')
    # 创建套接字
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)
    s.listen(5)

    #　忽略子进程信号
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)

    while True:
        try:
            c,addr = s.accept()
            print('Connect from',addr)
        except KeyboardInterrupt:
            s.close()
            sys.exit('服务器退出')
        except Exception as e:
            print(e)
            continue
        # 创建子进程
        pid = os.fork()
        if pid == 0:
            print('子进程准备处理请求')
            sys.exit('子进程退出')
        else:
            c.close()
            continue

if __name__ == '__main__':
    main()


