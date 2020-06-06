### 代码中的一些学习。

#### 4-1.py ：拉格朗日法插补

①：注意处理SettingWithCopyWarning的方法，通过查阅资料及尝试。

关于解决此问题的方法：（也有查阅到别的尝试后没有成功，后期若有遇到同样的问题遇到更好的方法会进行补充。）

将is_copy的标志设置为False

②：scipy库内的lagrange()函数的一些说明。名字就代表了它的作用，用于拉格朗日插值。

lagrange(x,y)的两个参数x,y就是已知数据量一一对应.

f = lagrange(x,y)。此处f的类型为：多项式对象 

<class 'numpy.lib.polynomial.poly1d'>。可像函数一样调用它。

简单举例：

```python
x = [1,2,3,4,5]
y = [1,2,3,4,5]
f = lagrange(x,y)
print(f(6))

#ouput: 6.00000000000004
```

#### 4-2.py :归一化数据的三种方法演示

①numpy库内的ceil（）函数：

返回输入值的上限，就是返回大于等于输入值的最小整数。（与int转化不同。）

举例：

```python
n = np.array([-1.9,-2.6,3,4,2.3])
print(np.ceil(n))

#output:[-1. -2.  3.  4.  3.]
```

#### 4-3.py :数据离散化三种方法的具体实现。

①pandas.**cut**(x,bins,right=True,labels=None,retbins=False,precision=3,include_lowest=False)

 相关参数说明：

x为被划分的一维数组。bins为划分为多少个区间。

labels : 是否用标记来代替返回的bins 。

②sklearn.KMeans函数的参数说明：

n_clusters:聚类中心数量，默认为8 

max_iter:算法运行的最大迭代次数，默认为300

tol:最小误差，当误差小于tol就退出。默认为1e-4

聚类算法的详情会后续补充。

相关输出：

1.等宽法：![没了。](https://github.com/doordiey/Python_data_analysis/blob/master/image/4-3-1.png)

2.等频率法：

![没了。](https://github.com/doordiey/Python_data_analysis/blob/master/image/4-3-2.png)

3.聚类法：

![没了。](https://github.com/doordiey/Python_data_analysis/blob/master/image/4-3-3.png)

#### 4-4.py :线损率属性构造

就很简单，进一步理解属性构造的具体表现。

#### 4-5.py :小波变换特征提取

关于小波变换理解还不多，后续补充。

①查阅文档了解pywt.wavedec函数相关内容。

参数：

**data**:array_like 就是输入的数据（此例中为信号文件）

**wavelet**:Wavelet object or name string  小波对象或名字。（此例中bior5为一种小波的名字。全称为 Biorthogonal （bior)。

**level**: int 分解等级（必须大于等于0）

**axis** :int 用于计算DWT的轴，如果没有给出，就使用最后一个轴。

[关于pywt库更详细内容的参考链接](https://pywavelets.readthedocs.io/en/latest/ref/dwt-discrete-wavelet-transform.html)

#### 4-6.py:主成分分析降维

①查阅文档了解sklearn.PCA函数相关内容。

参数：

**n_components**:int,float,None or string. 特性向量数，若不自行设置则默认为所有特性向量数。

**copy**:bool. 默认为True

**whiten**：bool 默认为False

**svd_solve** :string{‘auto’, ‘full’, ‘arpack’, ‘randomized’} 

[sklearn.PCA详细内容](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)

