#-*- coding:utf-8 -*-
import pandas as pd
catering_sale = '../../data/3-/catering_sale.xls'     #数据存储位置
data = pd.read_excel(catering_sale,index_col = u'日期') #读取文件信息，以日期列为索引列
print(data.describe())

# 以下为输出结果
#                              销量
# 非空值数               count   200.000000
#   平均值             mean   2755.214700
#   标准差             std     751.029772
#   最小值            min      22.000000
#　　　　             25%    2451.975000
#         　　　       50%    2655.850000
#             　　　   75%    3026.125000
#              　　　  max    9106.440000

