#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np

datafile = '../../data/4-/normalization_data.xls'
data = pd.read_excel(datafile,header= None)

print("最小--最大规范化")
print((data - data.min())/(data.max() - data.min()))
print("零--均值规范化")
print((data-data.mean())/data.std())
print("小数定标规范化")
print(data/10**np.ceil(np.log10(data.abs().max())))
