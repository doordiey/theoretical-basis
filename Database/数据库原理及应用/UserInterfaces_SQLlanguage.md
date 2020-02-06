# User Interfaces and SQL Language 用户接口与SQL语言

## User interface of DBMS

- DBMS必须提供一些接口给用户使用数据库，用户接口类型包括
  - 查询语言【核心】
    - 形式化查询语言
    - 表格式查询语言
    - 图形化查询语言
    - 受限制的自然语言查询
  - 访问数据库的工具（GUI）
  - API（解决在应用程序中访问数据库）
  - 类库

### 关系查询语言

- 查询语言：让用户有效的从数据库中检索需要的数据
- 关系模型支持简单，有力的查询语言
- 查询语言不是编程语言
  - 查询语言不是图灵完备的，不具备编程能力
  - 不能做复杂计算

#### 形式化基础

##### 数学化

- 关系代数 【过程化】
- 关系演算 【非过程化】

### SQL

- 数据定义语言【DDL】
- 查询语言【QL】
- 数据操纵语言【DML】
- 数据控制语言【DCL】

#### 重要术语与概念

- Base Table 基表
  - 关系模型中的关系【物理存在的】
- View 视图
  - 虚表  
- 数据类型
- NULL  
  - 保留字：空值
- UNIQUE
  - 保留字：表的某个属性是否允许有重复值
- DEFAULT
  - 保留字：为某张表的某个属性默认缺损值
- PRIMARY KEY
  - 保留字：主键
- FOREIGN KEY
  - 保留字：外键
- CHECK
  - 保留字：定义完整性约束

#### 基本的SQL查询

```sql
SELECT [DISTINCT] target-list
FROM     relation-list
WHERE   qualification
```

- 关系列表 relation-list  【查询设计的表】
- 目标列表  target-list    【要查询的东西】
- 条件   qualification   【布尔表达式】
- DISTINCT 可选字符，加了的话表明要求系统对查询结果的重复元组要消除。 

#### 查询语句执行的基本策略

- 把FROM子句里出现的表做笛卡尔乘积
- 把笛卡尔乘积的觉果用qualification做筛选
- 根据target-list 内的对上一步结果做投影
- 如果有DISTINCT，将重复元组筛选

##### 范围变量

- 即在FROM 内给表取别名，只要不会引起混淆，可以不加别名【下面的写法相同】

- 找出预定了船号为103的水手的姓名

  - ```sql
    SELECT S.sname  【最规范写法】
    FROM Sailors S,Reserves R
    WHERE S.sid = R.sid AND R.bid=103
    ```

  - ```sql
    SELECT S.sname
    FROM Sailors S,Reserves R
    WHERE S.sid = R.sid AND bid =103
    ```

  - ```
    SELECT sname
    FROM Sailors,Reserves
    WHERE Sailors.sid = Reserves.sid AND bid = 103
    ```

##### 例子：

- SELECT 不同时，慎重考虑是否要加DISTINCT

  - 找出至少预定过一次船的水手

  - ```sql
    SELECT S.sid
    FROM Sailors S,Reserves R
    WHERE S.sid = R.sid
    ```

  - 比如：此例中若将sid 改为sname 那么加不加DISTINCT对结果的意义就有影响。

- SELECT 子句中可以使用表达式

  - ```SQL
    SELECT S.age,age1=S.age-5,2*S.age AS age2   //给结果属性命名的两种办法【不一定两种方法都支持】
    FROM Sailors S
    WHERE S.sname LIKE 'B_%B'   //支持用like表达的模糊查询
    ```

- 用集合的交和并方式进行查找

  - 找出预定过一艘红船或者预定过一艘绿船的水手的编号

  - ```sql
    SELECT S.sid
    FROM Sailors S,Boats B,Reserves R
    WHERE S.sid =R.sid AND R.bid = B.bid AND(B.color='red' or B.color = 'green')
    ```

  - ```sql
    SELECT S.sid
    FROM Sailors S,Boats B,Reserves R
    WHERE S.sid =R.sid AND R.bid = B.bid AND B.color='red'【所有预定红船的水手编号】
    UNION
    SELECT S.sid
    FROM Sailors S,Boats B,Reserves R
    WHERE S.sid =R.sid AND R.bid = B.bid AND B.color = 'green'【所有预定绿船的水手编号】
    ```

  - 更新问题为：预定过红船和绿船的水手的标号

  - ```sql
    SELECT S.sid
    FROM Sailors S,Boats B1,Reserves R1,Boats B2,Reserves R2  【进行自连接】
    WHERE S.sid = R1.sid AND R1.bid=B1.bid AND S.sid=R2.sid AND R2.bid=B2.bid
    AND (B1.color='red' AND B2.color='green')
    【自连接方法效率不高】
    ```

  - ```sql
    SELECT S.sid
    FROM Sailors S,Boats B,Reserves R
    WHERE S.sid =R.sid AND R.bid = B.bid AND B.color='red'【所有预定红船的水手编号】
    INTERSECT 【集合的交不是每个数据库都支持】 
    SELECT S.sid
    FROM Sailors S,Boats B,Reserves R
    WHERE S.sid =R.sid AND R.bid = B.bid AND B.color = 'green'【所有预定绿船的水手编号】
    【集合的交操作】
    ```

  - ```sql
    SELECT S.sid 
    FROM Sailors S,Boats B,Reserves R 
    WHERE S.sid =R.sid AND R.bid = B.bid AND B.color = 'red' AND S.sid in ( SELECT S.sid 
    FROM Sailors S,Boats B,Reserves R 
    WHERE S.sid =R.sid AND R.bid = B.bid AND B.color = 'green' )
    【嵌套查询的方法】
    ```

  - 

- 嵌套查询

  - 找出预定了103号船的水手姓名

  - ```sql
    SELECT S.sname
    FROM Sailors S
    WHERE S.sid IN(SELECT R.sid
    	FROM Reserves R
    	WHRER R.bid=103)
    ```

  - 该例子为非关联嵌套，子查询只执行一次

  - ```sql
    SELECT S.sname
    FROM Sailors S
    WHERE EXISTS (SELECT *
    	FROM Reserves R
    	WHRER R.bid=103 AND S.sid =R.sid)
    ```

  - 该查询为关联嵌套，子查询要做多次【相当于二层循环】

  - 且只被一个水手预定过的船的编号：

  - ```sql
    SELECT  bid
    FROM Reserves R1
    WHERE bid NOT IN (
    		SELECT bid
    		FROM Reserves R2
    		WHERE R2.sid != R1.sid)
    ```

- 查找出一个水手级别比任何一个叫Horatio的水手级别高的

  - ```sql
    SELECT * 
    FROM Sailors S
    WHERE S.rating > ANY(
    	SELECT S2.rating
    	FROM Sailors S2
    	WHERE S2.sname = 'Horatio')
    ```

- 除法

  - 找出预定了所有船的水手

  - ```sql
    SELECT S.sname
    FROM Sailors S
    WHERE NOT EXISTS
    	((SELECT B.bid
    	FROM Boats B)  【所有的船】
    	EXCEPT   【减去】
    	(SLELECT R.bid 
    	FROM Reserves R
    	WHERE R.sid =S.sid)【该水手订过的船】
         【结果就是该水手没订过的船，若不存在，那么他就订过所有的船】
    	) 
    ```

  - ```sql
    SELECT S.sname
    FROM Sailors S
    WHERE NOT EXISTS(SELECT B.bid
    			FROM Boats B
    			WHERE NOT EXISTS(SELECT R.bid
    			FROM Reserves R
    			WHERE R.bid =B.bid
    			AND R.sid = S.sid
    			))
    			【双重否定表肯定】
    ```

### SQL语言内的函数运算

- COUNT* 
  - 统计关系里面有多少元组
- COUNT([DISTINCT]A)
  - 统计关系属性A有多少个不同的值
- SUM
  - 求和
- AVG 
  - 求平均值
- MAX
  - 求最大值
- MIN
  - 求最小值

#### 例子

```sql
SELECT COUNT *
FROM Sailors S 
【查找有多少个水手】
```

```sql
SELECT COUNT(DISTINCT S.rating)
FROM Sailors S
WHERE S.sname ='Bob'
【叫bob的有多少个级别】
```

##### 分组查询

###### 结构

- SELECT    target-list
- FROM    relation-list
- WHERE    qualification
- GROUP BY   grouping-list【将筛选后得到的结果通过group by进行分组得到grouping-list】
- HAVING    group-qualification 【对group by 得到的组进行筛选】

###### 概念化执行步骤

- 把 FROM子句中出现的表进行笛卡尔乘积，拼接起来
- 用where子句的qualification进行筛选
- 按照group-by将经过筛选后的元组进行分组
- 用having子句对分组进行筛选
- 将筛选后的组通过select子句进行运算，每一个组得到一个结果
- 要求，select 子句和having子句中的属性必须是group by分组属性值的子集

###### 例子

- 求出年龄大于18岁的水手里每个级别最年轻的水手，且级别组人数有2个以上

- ```sql
  SELECT S.rating,MIN(S.age) AS minage
  FROM Sailors S
  WHERE S.age>=18
  GROUP BY S.rating
  HAVING COUNT(*) >1
  ```

- 查每一条红船的预定人数有多少

- ```sql
  SELECT B.bid,COUNT(*) AS scount
  FROM Boats B,Reserves R
  WHERE R.bid = B.bid AND B.color='red'
  GROUP BY B.bid
  ```

- ```sql
  SELECT B.bid,COUNT(*) AS scount
  FROM Boats B,Reserves R
  WHERE R.bid = B.bid 
  GROUP BY B.bid
  HAVING B.color='red'
  【报错。此处的having属性的值不是group by的子集】
  ```

  

- 找出年龄大于18的各个级别中的最小年龄，级别人数至少为两人（任意年龄）

- ```sql
  SELECT S.rating,MIN(S.age)
  FROM Sailors S
  WHERE S.age>18
  GROUP BY S.rating
  HAVING 1<(SELECT COUNT(*)
  	FROM Sailors S2
  	WHERE S2.rating=S.rating)
  ```

- 查找平均年龄最小的级别

- ```sql
  SELECT Temp.rating
  FROM (SELECT S.rating,AVG(S.age)AS avgage
  	FROM Sailors S
  	GROUP BY S.rating)AS Temp
  WHERE Temp.avgage = (SELECT MIN(Temp.avgage)
  FROM Temp)
  ```

- FROM语句里面也可以嵌套查询

#### 空值问题

- 空值是不知道，是没有。

- 需要一些特别的操作判断是否为空
- 考虑空值与布尔表达式的影响
- 需要三级逻辑（真、假、不知道）

### 一些扩展

#### CAST表达式

- 类似于C、C++的强制类型转换
- CAST + NULL(Expression)  AS  Data type

##### 作用

- 符合函数语法
- 改变计算精度
- 给空值赋予数据类型

#### CASE表达式

- 可以简单的做条件判断

##### 用法

- ```sql
  CASE 
  	WHEN type='chain saw' THEN accidents 
  	ELSE 0e0
  END
  ```

#### 子查询

- 一个查询里面嵌套着查询就是子查询

##### 类型

- 标量子查询

  - 查询结果就是单个的值
- 表表达式

  - 查询结果是一张表
- 公共表表达式

  - 在一些复杂的查询中，一个表表达式可能需要用到多次，将它只定义一次，多次调用结果

- - 用with子句可以定义公共表表达式【相当于是一个临时视图】

  - 例子

    - 找出哪个部门的工资最高

    - ```sql
      WITH payroll(deptno,totalpay) AS(SELECT deptno totalpay
      	FROM emp
      	GROUP BY deptno)
      SELECT deptno
      FROM payroll
      WHERE totalpay=(SELECT max(totalpay)
      	FROM payroll)
      ```

#### Outer Join 外连接

- EXCEPT和EXCEPT ALL
  - 都是做集合差，但EXCEPT ALL 不删重复元组，也就不用排序，效率比EXCEPT高
- 用UNION ALL对多个SELECT结果并起来【这就是外连接】

#### 递归查询

- 在公共表表达式中用了自己的查询就是递归查询

##### 例子：

- ```sql
  WITH agents(name,salary) AS
  ((SELECT name,salary    【initial query】
   FROM FedEmp
   WHERE manager='Hoover')
  UNION ALL
  (SELECT f.name,f.salary   【recursive query】
  FROM agents AS a,FedEmp AS f
  WHERE f.manager=a.name))
  SELECT name 【final query】        
  ```

- 飞机零件例子【有向无环图】

- 飞机航班例子【有向有环图】

  - 控制递归的结束条件

### 数据操纵语言

- DELETE

  - 把表内满足条件的元组删除

- UPDATE

  - 把满足条件的元组的某些值进行更新

- Insert

  - 向表内插入元组

  - 例子

    - ```sql
      Insert into employees values("smith")
      ```

### SQL中的视图

##### 分类及相关介绍

- 普通视图【虚表】
  - 实现外模式
  - 利用视图和逻辑模式的映射实现数据的逻辑独立性
  - 数据库只存储视图的定义，不存储数据，数据在调用时临时计算，数据内容非永久保存
  - 实现了数据库的安全性
  - 对视图内数据的修改的问题
- 临时视图【公共表表达式】
  - 没有存储视图的定义
  - 可以实现递归查询

### 嵌入式SQL

- 为了实现和程序设计语言结合，解决的问题
  - 如何让程序设计语言接收SQL语言
  - DBMS和应用程序如何交换数据和信息
  - DBMS的查询结果是个集合，如何传递给程序设计语言中的变量
  - DBMS支持的数据类型和应用程序支持的数据类型不是完全一样

#### 解决方法

- 嵌入式SQL
- 编程的API
- 封装的类

##### 以C语言中的嵌入式SQL

- 以ECEC SQL,开始，以；结尾会被预编译器识别为嵌入式SQL命令
- 用宿主变量在DBMS和应用程序之间交换数据和消息
- 在SQL命令里，可以用：的方法引用宿主变量的值
- 宿主变量在C语言中就当一个普通的变量使用
- 不可以把宿主变量定义为数组或结构
- 一个特殊的宿主变量，通过SQLCA在C和DBMS进行数组交换
- SQLCA.SQLCODE 可以判断查询结果
- 用说明符来表示宿主变量的NULL

###### 定义数组变量

```c
EXEC SQL BEGIN DECLARE SECTION;
char SNO[7];
char GIVENSNO[7];
char CNO[6];
char GIVENCNO[6];
float GRADE;
short GRADE1;
EXEC SQL END DECLARE SECTION;
```

###### 执行命令的方式

- 连接

```c
EXEC SQL CONNECT :uid IDENTIFIED BU:pws: ;
```

- 执行DML语句

```c
EXEC SQL INSERT INTO SC(SNO,CNO,GRADE)VALUES(SNO,:CNO,:GRADE);
```

- 查询【简单查询，返回一个值】

```C
EXEC SQL SELECT GRADE INTO :GRADE,:GRADE1
FROM SC
WHERE SNO=:GIVENSNO AND CNO=:GIVENCNO;
```

为了处理查询返回的集合，引入游标机制

###### Cursor游标的操作步骤

- 定义游标

  - ```
    EXEC SQL DECLARE 游标名 CURSOR FOR
    SELECT
    FROM 
    WHERE
    ```

- 执行游标【可以理解为打开一个文件】

  - ```c
    EXEC SQL OPEN 游标名
    ```

- 取游标内每一条元组

  - ```c
    EXEC SQL FETCH 游标名
    	INTO  :hostvar1,:hostvar2;
    ```

- 判断查询结果是否取完

  - SQLCA.SQLCODE ==100 时取完

- 关闭CURSOR

  ```c
  CLOSE CURSOR
  ```

#### 动态SQL

上一个例子运用CURSOR的SQL语句是确定的，为了实现动态的SQL，

- 可以直接运行的动态SQL【非查询】
- 动态SQL的查询【带动态参数】
- 动态构造查询语句

##### 例子

- 可以直接运行的动态SQL【非查询】

  - 用字符数组动态拼接出一条sql语句

  - ```c
    EXEC SQL EXECUTE IMMEDIATE :sqlstring;
    ```

  - 让系统动态的及时执行sqlstring中的sql语句

- 动态SQL的查询【带动态参数】

  - 运用占位符

  - ```c
    EXEC SQL PREPARE PURGE FROM :sqlstring;【sql命令执行准备】
    EXEC SQL EXECUTE PURGE USING:birth_yers;【将参数替换】
    ```

- 动态构造查询语句

  - 用字符数组动态拼接出一条查询语句

  - ```c
    EXEC SQL PREPARE query FROM :sqlstring;   【先准备一下查询语句】
    EXEC SQL DECLARE grade_cursor CURSOR FOR query; 【建立一个游标】
    EXEC SQL OPEN grade_cursor USING :GIVENCNO; 【在此处替换占位符】
    ```

### 存储过程机制

- 允许用户把一组常用的sql定义为一个存储过程，系统对其优化编译后可以被直接调用。
  - 用户使用更加方便，应用需求发生变化时，只需要改变存储过程
  - 改进性能
  - 可以扩展DBMS的功能



