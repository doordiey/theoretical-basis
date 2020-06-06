#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt 

catering_sale = '../../data/3-/catering_sale.xls'
data = pd.read_excel(catering_sale,index_col = u'日期')
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False#用来正常显示负号

plt.figure() 
p = data.boxplot(return_type = 'dict')    #就是这里改一下。 
x = p['fliers'][0].get_xdata()  #fliers为异常值的标签。
y = p['fliers'][0].get_ydata()
y.sort()

#用annotate添加注释
# 第一个参数是注释的内容
# xytext设置注释内容显示的起始位置
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy = (x[i],y[i]),xytext = (x[i]+0.05 - 0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy = (x[i],y[i]),xytext = (x[i]+0.08,y[i]))
plt.show()
