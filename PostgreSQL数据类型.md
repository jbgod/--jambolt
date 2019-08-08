# 数据类型



![1565074260622](C:\Users\LQ\AppData\Roaming\Typora\typora-user-images\1565074260622.png)

![1565074294829](C:\Users\LQ\AppData\Roaming\Typora\typora-user-images\1565074294829.png)

### 类型的输入与转换

简单的数据类型

```
postgres=# select 1, 3.1415, '3.14444';
 ?column? | ?column? | ?column? 
----------+----------+----------
        1 |   3.1415 | 3.14444
(1 row)
```

用类型名转换

```
postgres=# select int '1'+int '3';
 ?column? 
----------
        4
(1 row)
postgres=# select bit '10101111';
   bit    
----------
 10101111
(1 row)
postgres=# select date '10101111';
    date    
------------
 1010-11-11
(1 row)
postgres=# select cidr '1.1.1.1';
    cidr    
------------
 1.1.1.1/32
(1 row)
postgres=# select 'xff'::bit(16);
       bit        
------------------
 1111111100000000
(1 row)
```

### 1.布尔型数据

boolean 有 true  false   不带引号的 TRUE FALSE

布尔型的操作符

AND 与 OR 或 NOT 非



### 2.数值类型

数值型

![1565080866610](C:\Users\LQ\AppData\Roaming\Typora\typora-user-images\1565080866610.png)

整形int smallint bigint

序列类型 sequence

字符型

![1565081096478](C:\Users\LQ\AppData\Roaming\Typora\typora-user-images\1565081096478.png)

枚举类型

​	有序的静态值集合的数据类型

XML类型

xml函数处理xml数据

