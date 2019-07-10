# Random forest 

import pandas as pd 
import os
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.metrics import confusion_matrix
from sklearn import metrics

basedir='E:/DE/Sem2/AdvancedProject/bbdc_2019_Bewegungsdaten/'

# Reading training file for label
train_file=pd.read_csv('E:/DE/Sem2/AdvancedProject/bbdc_2019_Bewegungsdaten/train.csv',delimiter=',')
labels=train_file['Label']
encoder = preprocessing.LabelEncoder()
encoder.fit(labels)
activity_labels_nums = encoder.transform(labels)

basedir='E:/DE/Sem2/AdvancedProject/bbdc_2019_Bewegungsdaten'
def file_processing(foldername):
    for filename in os.listdir(os.path.join(basedir,foldername)):
        #print (filename)
        f=open((basedir+'/'+foldername+'/'+filename),'r')
        file_arr=[]
        #file_arr=np.zeros(6159)
        for line in f:
            li_st=line.split(',')
            arr_st=np.array(li_st)
            arr_fl=((arr_st).astype(np.float))
            #print (arr_fl)
            file_arr.append(arr_fl)
            final_li=(np.array(file_arr)).reshape(1,5569*19)
#print(np.array(final_li).shape)

X_train, X_test, y_train, y_test = train_test_split(df, activity_labels_nums[1:4], test_size=0.3) # 70% training and 30% test
clf=RandomForestClassifier(n_estimators=100)
clf.fit(X_train,y_train)

y_pred=clf.predict(X_test)
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
