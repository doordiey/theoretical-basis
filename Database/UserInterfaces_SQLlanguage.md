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

- 即在FROM 内给表取别名，只要不会引起混淆，可以不加别名

##### 例子：

- SELECT 不同时，慎重考虑是否要加DISTINCT

- SELECT 子句中可以使用表达式

  - ```SQL
    SELECT S.age,age1=S.age-5,2*S.age AS age2   //给结果命名的两种办法
    FROM Sailors S
    WHERE S.sname LIKE 'B_%B'   //模糊查询
    ```



