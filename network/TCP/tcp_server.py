﻿# 导入 socket 库
import socket
import time, threading


def test_server():
    # 创建一个socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 监听端口
    s.bind(('127.0.0.1', 9999))

    # 开始监听端口，最大连接数为5
    s.listen(3)

    print('Waiting for connection...')

    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(2)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == "__main__":
    test_server()