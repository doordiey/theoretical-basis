#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

datafile = '../../data/4-/discretization_data.xls'
data = pd.read_excel(datafile)
data = data['肝气郁结证型系数'].copy()
k=4
d1 = pd.cut(data,k,labels = range(k)) #等宽离散化，并给每个类别命名。

w = [1.0*i/k for i in range(k+1)]
w = data.describe(percentiles = w)[4:4+k+1] #使用describe函数计算分位数
w[0] = w[0]*(1-1e-10)
d2 = pd.cut(data,w,labels= range(k))

kmodel = KMeans(n_clusters= k, n_jobs= 1) #建立模型，n_jobs使并行数
kmodel.fit(data.values.reshape((len(data),1)))
c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0) #输出聚类中心，并且排序
w = pd.rolling_mean(c,2).iloc[1:]
w = [0] + list(w[0]) +[data.max()]
d3 = pd.cut(data,w,labels=range(k))

def cluster_plot(d,k):#画图a
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False

	plt.figure(figsize= (0,3))
	for j in range(0,k):
		plt.plot(data[d == j],[j for i in d[d==j]],'o')
	plt.ylim(-0.5,k-0.5)
	return plt

if __name__ == "__main__":
	cluster_plot(d3,k).show()
	# cluster_plot(d1, k).show()
	# cluster_plot(d2, k).show()