# coding=utf-8

import numpy as np

score=np.load('.\\results\ROC\score_vector.npy')
target=np.load('.\\results\ROC\\target_label_vector.npy')
model=np.load('.\\results\Model\\MODEL.npy')
cc=score.reshape(12,4)
print('aa')
pass