"""
客户端
接下来我们写一个简单的客户端实例连接到以上创建的服务。端口号为 9999。

socket.connect(hosname, port ) 方法打开一个 TCP 连接到主机为 hostname 端口为 port 的服务商。连接后我们就可以从服务端获取数据，记住，操作完成后需要关闭连接。

完整代码如下：
"""
# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 10999

# 连接服务，指定主机和端口
client_socket.connect((host, port))

# 接收小于 1024 字节的数据
msg = client_socket.recv(1024)

client_socket.close()

print(msg.decode('utf-8'))
