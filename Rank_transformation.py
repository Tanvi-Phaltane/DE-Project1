#________
# Rank transformation of data
# Tanvi
#________

import os
import numpy as np
import collections
from class_rank import Rank

basedir='E:/DE/Sem2/AdvancedProject/bbdc_2019_Bewegungsdaten'
def file_processing(foldername):
    for filename in os.listdir(os.path.join(basedir,foldername)):
        print (filename)
        f=open((basedir+'/'+foldername+'/'+filename),'r')
                    #f=open((os.path.join(basedir,foldername,filename)),"r")
        f_out=open("rank_file_"+filename+".txt","w")
        for line in f.readlines():
        #print (line)
        line=line.rstrip().split(',')
        #print (line)
        ind=list(np.argsort(line))        # sorting list to get indices
        #print (ind)
        #print(type(ind))           # ind is an array
        rank_dict={}                # creating a dictionary with key as no. and value as rank
        freq_dict={}                # if duplicate nos than freq table
        arr=np.array(line)          # converting line to array
        #print (arr)
        min_no=np.min((arr).astype(np.float))          # minimum num in array
#Rank  calculation: rank = Lx + 1/Ix(sum(i))  Lx = nos. less than given no.  Ix=no.of repetitive nos  
        for i in range(len(arr)):
            num=arr[i]
            ob=Rank()
            freq_dict2=ob.freq(num,freq_dict)
            ix=ob.ix_fun(freq_dict2,num)
            lx=ob.lx_fun(ind,arr,num,min_no,i)
            rank_num=ob.rank_fun(lx,ix)
            rank_dict[num]=rank_num
            #print(num,rank_dict[num])
            #f_out.write('{}-'.format(num))
            f_out.write('{}\t'.format(rank_dict[num]))
            f_out.write('\n')
        f_out.close()

for i in range(1,20):
    if i < 10:
        foldername='Subject0{}'.format(i)
#        print(foldername)
        file_processing(foldername)
    if i>=10:
        foldername='Subject{}'.format(i)
        file_processing(foldername)
#        print(foldername)
        


    
