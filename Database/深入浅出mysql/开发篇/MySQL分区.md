# MySQL分区

## 概述

> 分区是指根据一定的规则，数据库把一个表分解成多个更小的、更容易管理的部分。

``` sql
show variables like '%partition%';//确定当前的Mysql是否支持分区
```

分区的优点：

- 和单个磁盘或者文件系统分区相比，可以存储更多数据
- 优化查询
- 对于已经过期或者不需要保存的数据，可以通过删除与这些数据有关的分区来快速删除数据
- 跨多个磁盘来分散数据查询，获得更大的查询吞吐量

## 分区类型

> RANGE分区、LIST分区、HASH分区都要求分区键必须是INT类型，或通过表达式返回INT类型，唯一例外的是KEY分区，可以使用其它类型的列作为分区键。
>
> 不能使用主键/唯一键字段之外的其它字段分区。
>
> 分区的名字基本遵循MySQL标识符的原则。

### RANGE分区

> 基于一个给定连续区间范围，把数据分配到不同的分区

eg:雇员表emp中按商店ID store_id 进行RANGE分区

``` mysql
create table emp(
	id int not null,
	ename varchar(20),
	hired data not null default '1970-01-01',
	sparated data not null default '9999-12-06',
	job varchar(30),
	stored_id int not null
)
partition by range(store_id)(
	partition p0 values less then(10),
    partition p0 values less then(20),
    partition p0 values less then(30),
);
```

- 此时无法插入商店ID大于等于30的，分区规则没有包含，不知道要保存在哪里。
  - ` alter table emp add partition(partition p3 values less than maxvalue);`

- RANGE分区中，如果分区键是NULL值会被当作一个最小值来处理
- 想在日期或者字符列上进行分区，需要使用函数进行转换，查询如果不用转换的话，无法达到分区优化查询性能的效果

#### 适用场景

- 需要删除过期的数据时，直接drop对应分区的内容，比delete运行有效
- 经常运行包含分区键的查询

### List分区

> 建立离散的值列表告诉数据库特定的值属于哪个分区，类似于RANGE分区，区别在于LIST分区时从属于一个枚举列表的值的集合，RANGE分区是从属于一个连续区间值的集合。

eg:建一个List分区

```mysql
create table expenses(
	expense_date date not null,
	category int,
	amount decimal(10,3)
)partition by LIST(category)(
	partition p0 values in (3,5),
    partition p1 values in (1,10),
    partition p2 values in (4,9),
    partition p3 values in (2),
    partition p4 values in (6),
	);
```

- 要匹配的值必须在值列表中找得到

### Columns分区

> 解决RANGE分区和LIST分区只支持整数分区，需要额外的函数计算来转换的问题

#### 支持的数据类型

- 所有整数类型
- 日期时间类型：date和datetime
- 字符类型：char,varchar,binary,varbinary,不支持text和blob类型作为分区键

#### 支持多列分区

eg:实例

``` mysql
create table rc3(
	a int,
	b int
)
partition by range columns(a,b)(
	partition p01 values less than (0,10),
    partition p01 values less than (10,10),
    partition p01 values less than (10,20),
    partition p01 values less than (10,35),
    partition p01 values less than (10,maxvalue),
    partition p01 values less than (maxvalue,maxvalue),
);
```

- 分区键的比较是多列排序，先根据a字段排序再根据b字段排序，根据排序结果来分区存放数据

### Hash分区

> 主要用来分散热点读，确保数据再预先确定个数的分区中尽可能平均分布。

#### 常规HASH分区

> 取模算法

eg:创建一个基于store_id列的HASH分区表，划分成4个分区

``` mysql
create table emp(
	id int not null,
	ename varchar(20),
	hired data not null default '1970-01-01',
	sparated data not null default '9999-12-06',
	job varchar(30),
	stored_id int not null
)
partition by hash(store_id) partitions 4;
```

- 通过取模的方式数据尽可能平均分布，每个分区管理的数据都减少了，提高了查询的效率
- 缺点：当要新增一个常规分区的话，原来分区中的数据大部分需要通过计算重新分区

#### 线性HASH分区

> 线性的2的幂的运算法则

eg: 创建一个线性hash分区

```
create table emp(
	id int not null,
	ename varchar(20),
	hired data not null default '1970-01-01',
	sparated data not null default '9999-12-06',
	job varchar(30),
	stored_id int not null
)
partition by Linear hash(store_id) partitions 4;
```

- 优点：分区维护时处理迅速
- 缺点：各个分区之间数据的分布不太均匀

##### 计算过程

- 找到下一个大于等于分区数的2的幂，这个值设为V
- 设置N =F（column_list)&(V-1)
- 当N>=num ，N=N&(V-1)

### key分区

> 类似HASH分区，不过HASH分区允许使用用户定义的表达式，而Key分区不允许使用用户自定义的表达式，需要使用服务器提供的hash函数，支持使用除blob或text类型外其它类型的列作为分区键

eg: 创建key分区表

``` mysql
create table emp(
	id int not null,
	ename varchar(20),
	hired data not null default '1970-01-01',
	sparated data not null default '9999-12-06',
	job varchar(30),
	stored_id int not null
)
partition by Linear key(job) partitions 4;
```

- 创建key分区表时，可以不指定分区键，默认会首先选择使用主键做分区键，没有主键的情况下会选择非空唯一键作为分区键，如果都没有就必须指定

### 子分区

> 就是复合分区，对分区进行再次分割

eg:例子

```mysql
create table ts(id int,purchased date)
	partition by RANGE(YEAR(purchased))
	subpartition by hash(to_days(purchased))
	subpartitions 2(
    	parpition p0 values less than （1990)，
    	parpition p0 values less than （1999)，
    	parpition p0 values less than maxvalue，
    )；
    	
```

### MySQL分区处理null值

> 一般情况下，MYSQL分区把null当作零值，或者一个最小值进行处理

- RANGE分区：当作最小值处理
- LIST分区：必须出现再枚举列表中，否则不被接收
- HASH/KEY分区，当作零值处理

## 分区管理

- 添加
- 删除
- 重定义
- 合并
- 拆分

> 都可以通过alter table命令实现

### RANGE&LIST分区管理

- 在添加、删除、重新定义分区的处理上类型

#### 删除

```mysql
alter table tablename drop partition 
```

#### 增加

``` mysql
alter table tablename add partition
```

### HASH&KEY分区管理

#### 删除

``` mysql
alter table tablename coalesce partition 2;
```

#### 增加

```mysql
alter table tablename add partition partitions num;
```

