# SQL优化

## 优化SQL语句的一般步骤

### 通过`show status`命令了解SQL的执行频率

- 如果不加global参数，显示的是当前连接的统计结果，显示执行每个语句的次数
- 比较关注的一些统计参数
  - Com_select:执行select操作的次数
  - com_select：执行insert操作的次数，批量插入只累加1
  - com_update:执行update操作的次数
  - com_delete:执行delete操作的次数
- 还有只针对innodb存储引擎的
  - innodb_rows_read:select查询返回的行数
  - innode_rows_inserted:insert操作插入的行数
  - …

### 定位执行效率较低的SQL语句

- 通过慢查询日志定位执行效率低的SQL语句
- 可以使用`show processlist`查看当前mysql在进行的线程，包括线程的状态，是否锁表等，可以试试查看SQL的执行情况

### 通过`explain`分析低效SQL的执行计划

> mysql引入了explain extended命令，通过explain extended加上show warnings可以看到sql真正执行前优化器做了哪些SQL改写

#### explain参数说明

- select_type:表示类型，有简单表【不用表连接或子查询】、主查询【即外层的查询】、union【Union中的第二个或者后面的查询语句、subquery【子查询中第一个select】
- table：输出结果集的表
- type：表示MYSQL在表种找到所需行的方式，访问类型
  - type=all:全表扫描
  - type=index：索引全扫描
  - type=range:索引范围扫描
  - type=ref：使用非唯一索引扫描或唯一索引的前缀扫描
  - type=eq_red：类似ref，区别在于使用的索引是唯一索引
  - type=const/system，单表中最多有一个匹配行
  - type=null，不用访问表或索引，直接得到结果

### 通过`show profile`分析SQL

> 能够更情况的了解SQL执行过程

- 还可以进一步选择all、cpu、…等明细类型查看在使用什么资源上耗费了时间

### 使用trace分析优化器如何选择执行计划

