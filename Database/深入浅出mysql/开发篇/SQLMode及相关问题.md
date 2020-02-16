# SQL Mode及相关问题

> 不同的SQL Mode定义了支持的SQL语法、数据校验等。

## 简介

- 通过设置SQL Mode可以完成不同严格程度的数据校验，有效地保障数据准确性
- 通过设置SQL Mode位ANSI模式，可以保证大多数SQL符合标准的SQL语法，可以在数据库迁移时，不需要对业务SQL进行较大的修改
- 在不同的数据库进行迁移之前可以通过SQL Mode的修改更方便的进行迁移

> 简单实例：使用SQL Mode始先数据校验
>
> ```mysql
> select @@sql_mode; //查看默认的SQLMode
> insert into my values(1111111111111111111111,111111111111111,'yyy');//故意插入超出实际定义值int(11),提示错误，无法插入
> set session sql_mode='ANSI';//修改sql_mode
> insert into my values(1111111111111111111111,111111111111111,'yyy');//插入成功，提示有一个warning
> ```

- session表示只在本次连接中生效，而global选择表示在本次连接中并不生效，对新的连接生效

## 常见功能

- 校验日期数据合法性
  - 在ANSI模式下，非法日期可以插入，但会变成“0000-00-00 00：00：00‘，并给出warning
  - 在TRADTIONAL模式下，会直接提示日期非法，拒绝插入
- 在insert或update过程中，如果处于TRADTIONAL模式，那么运行MOD（X，0）会产生错误，而非严格模式下，会返回null
  - TRADTIONAL属于严格模式
- 启用NO_BACKSLASH_ESCAPES模式，使反斜线成为普通字符，在导入数据时可保证数据的正确性
- 启用PIPES_AS_CONCAT模式，将"||"视为字符串连接操作符

## 常用的SQL Mode

> 实际应用时，可以设置一个模式组合，然后设置很多的原子模式

| sql_mode            | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| ANSI                | 等同于REAL_AS_FLOAT、PIPES_AS_CONCAT、ANSI_QUOTES、IGNORE_SPACE和ANSI组合模式，使语法和行为更符合标准的SQL |
| STRICT_TRANS_TABLES | 适用于事务表和非事务表，是严格模式，不允许非法日期，也不允许超过字段长度的值插入字段中，对于插入不正确的值给出错误而不是警告 |
| TRADTIONAL          | 可以应用在事务表和非事务表，用在事务表时，只要出现错误就会回滚 |

## SQL Mode在迁移中如何使用

> 提供了很多数据库的组合模式名称

| 组合后模式名称 | 组合模式中的各个sql_mode                                     |
| -------------- | ------------------------------------------------------------ |
| DB2            | pipes_as_concat、ANSI_QUOTES、IGNORE_SPACE、NO_KEY_OPTIONS、NO_TABLES_OPTIONS、NO_FIELD_OPTIONS |
| MAXDB          | pipes_as_concat、ANSI_QUOTES、IGNORE_SPACE、NO_KEY_OPTIONS、NO_TABLES_OPTIONS、NO_FIELD_OPTIONS、NO_AUTO_CREATE_USER |
| MSSQL          | pipes_as_concat、ANSI_QUOTES、IGNORE_SPACE、NO_KEY_OPTIONS、NO_TABLES_OPTIONS、NO_FIELD_OPTIONS |
| ORACLE         | pipes_as_concat、ANSI_QUOTES、IGNORE_SPACE、NO_KEY_OPTIONS、NO_TABLES_OPTIONS、NO_FIELD_OPTIONS、NO_AUTO_CREATE_USER |
| POSTGRESQL     | pipes_as_concat、ANSI_QUOTES、IGNORE_SPACE、NO_KEY_OPTIONS、NO_TABLES_OPTIONS、NO_FIELD_OPTIONS |

