- 记录自己在MySQL登陆使用遇到的相关问题

### 虚荣心作祟：

- 可能是电视剧看多了吧，总觉得对着个黑框框【cmd命令行】操作帅的不行。windows强行linux感。

- 命令行登陆命令: mysql -u '用户名' -p '密码'

![login-cmd](./picture/login-cmd.png)

##### 注意：要这样耍帅要记得将Mysql设置环境变量：

![setpath](./picture/setpath.png)



### 没记性的脑子：

- 现如今，各种设备、各种密码。忘记也是人的本性。
- 久病成医。

##### 操作如下：

- 停止MySQL服务
- 在cmd窗口输入命令：mysqld --skip-grant-tables
- 然后再开一个cmd,运行mysql进去修改mysql表内用户信息。
- 修改完成后重新开启mysql服务。