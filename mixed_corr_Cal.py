# merging correlation calculation for rank and real valued files -> plotting heat map
# Tanvi
# date: 06/06/19
# _______

from scipy.stats import spearmanr
from random import randint
import csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# defining a list for feature names
dict_feat_names={}
for i in range(1,20):
        sensor_name="s{}".format(i)
        dict_feat_names[sensor_name]=[]
#print (dict_feat_names)


# adding values to each feature (storing columns)
with open('E://DE//Sem2//AdvancedProject//bbdc_2019_Bewegungsdaten//Subject02//Subject02_Aufnahme000.csv') as csvfile:
    reader = csv.reader(csvfile,delimiter=',')
    for row in reader:
        for i in range(1,20):
            #print ([i])
            dict_feat_names['s{0}'.format(i)].append(row[i-1])

df=pd.DataFrame.from_dict(dict_feat_names)
corr_out=df.astype(float).corr(method='spearman')
#print(corr_out.iloc[:,0])
corr_out=round(corr_out,2)
corr_out.to_csv('spearmanCorrelationRealOut.tsv',sep='\t')
##########################################

## ** Rank file ** ##
# defining a list for feature names
dict_feat_names_rk={}
for i in range(1,20):
        sensor_name2="s{}".format(i)
        dict_feat_names_rk[sensor_name2]=[]
#print (dict_feat_names_rk)


# adding values to each feature (storing columns)
with open('rank_file.txt') as tsvfile:
    reader2 = csv.DictReader(tsvfile,dialect='excel-tab')
    for row in reader2:
        for i in range(1,20):
            #print (row['s{0}'.format(i)])
            dict_feat_names_rk['s{0}'.format(i)].append(row['s{0}'.format(i)])   
#            mean_rk+=row['s{0}'.format(i)]

#f_sp=open('spearmanCorrelationEffOut.tsv','w')

df2=pd.DataFrame.from_dict(dict_feat_names_rk)
corr_out_rk=df2.astype(float).corr(method='spearman')
corr_out_rk=round(corr_out_rk,2)
corr_out_rk.to_csv('spearmanCorrelationEffOut.tsv',sep='\t')
#print (corr_out_rk.iloc[18][18])
##########################
# calculating difference between real-valued correlations and rank-based correlations
fw=open("Corr_diff.txt",'w')
corr_mat=[]
for i in range(0,19):
    for j in range (0,19):
        diff=corr_out.iloc[i][j] - corr_out_rk.iloc[i][j]
        diff=round(diff,2)
        corr_mat.append(diff)
        fw.write("{}\t".format(diff))
    fw.write("\n")
fw.close()
result=np.reshape(corr_mat,(19,19))
ax = sns.heatmap(
    result, 
    vmin=-1, vmax=1, center=0,
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)

