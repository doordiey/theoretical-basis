#-*- coding:utf-8 -*-
import pandas as pd
from scipy.interpolate import lagrange

inputfile = '../../data/4-/catering_sale.xls'
outputfile = '../../data/4-/sales.xls'

data = pd.read_excel(inputfile)
m = data[u'销量'][(data[u'销量'] < 400 ) | (data[u'销量'] > 5000)]
m.is_copy = False
m = None
#选出异常值，将其置为空值。(此处与书上有改动。)
#书上直接赋值，会出现ettingWithCopyWarning。尝试对一个dareFrame的copy进行辅助。
# 为解决这个报错，就将m的is_copy设置为False,再进行赋值，可以解决此问题。

#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数。
def ployinterp_column(s,n,k):
	y = s[list(range(n-k,n)) + list(range(n+1,n+1+k))] #取数
	y = y[y.notnull()] #除去空值

	return lagrange(y.index,list(y))(n)  #插值并返回结果

for i in data.columns:
	for j in range(len(data)):
		if (data[i].isnull())[j]: #如果为空就进行插值。
			data[i][j] =ployinterp_column(data[i],j,5)
data.to_excel(outputfile)