#-*- coding:utf-8 -*-
from scipy.io import loadmat
import pywt


inputfile = '../../data/4-/leleccum.mat'  #提取自matlab的信号文件。
mat = loadmat(inputfile)
print(mat)
sigal = mat['leleccum'][0]
coeff =pywt.wavedec(sigal,'bior3.7',level=5)
