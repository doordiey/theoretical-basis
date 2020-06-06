#-*- coding:utf-8 -*-
import pandas as pd

inputfile = '../../data/4-/electricity_data.xls'
outpufile = '../../data/4-/out_electricity_data.xls'

data = pd.read_excel(inputfile)
data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量'])/data[u'供入电量']

data.to_excel(outpufile,index = False)
