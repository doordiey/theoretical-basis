import pandas as pd
from sklearn.decomposition import PCA

inputfile = '../../data/4-/principal_component.xls'
outputfile = '../../data/4-/dimention_reducted.xls'
data = pd.read_excel(inputfile,header= None)

pca = PCA()
pca.fit(data)
print(pca.components_)#返回各个特征向量
print(pca.explained_variance_ratio_)#返回各个成分各自的方差百分比