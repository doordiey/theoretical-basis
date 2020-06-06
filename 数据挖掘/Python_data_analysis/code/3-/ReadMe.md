# 代码中的一些学习：

#### 3-1.py :    pandas库内describe()函数。

当数据记录较大时，可用describe()函数看出是否有缺失值，以及最大值，最小值等数据的基本特征。

#### 3-2.py:箱线图显示异常值

若按照书中代码输出会报错出现：

TypeError: 'AxesSubplot' object has no attribute '__getitem__'。

产生原因是p在data.boxplot()返回对象不行，将返回类型指定一下。然后就可以了。

输出结果为：![没了。](https://github.com/doordiey/Python_data_analysis/blob/master/image/3-2.png)

#### 3-3.py:3-1的部分改良。

说明了两点：

一。说明可以根据了；列表内的值进行筛选处理。

二。说明可以对整列数据进行加减乘除的处理，以得到自己想看到的数据。

####  3-4.py:菜品盈利的贡献度分析图

其中有两个函数说明一下：

pandas.cumsum()函数为返回给定axis上的累计和函数。(就是累加.)

matplotlib.annotate()函数相关参数说明：

例：annotate(s='str' ,xy=(x,y) ,xytext=(l1,l2) ,..)

其中：

s 为注释文本内容 ，xy 为被注释的坐标点即（x,y)，xytext 为注释文字的坐标位置。

arrowprops 为箭头参数其参数类型应为字典类型。

其中：arrowstyle和connectionStyle为进一步设定箭头样式，可以有更多样子，需要的可以了解更多参数，进行调整。）

输出结果为：![没了。](https://github.com/doordiey/Python_data_analysis/blob/master/image/3-4.png)

#### 3-5.py:计算相关系数函数（由此判断两个变量之间是否相关）

注：当相关系数越接近１，说明相关性越强。

corr()函数为计算相关系数的函数，代码中提供了三种呈现。

注：此处为Pealson相关系数，故输入的参数也应满足Pealson相关系数的条件。即两个连续性变量。





