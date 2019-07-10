class Rank(object):
	def __init__(self):
		#self._freq_dict[num]=0
		self._rank_num=-1
		#self._rank_dict[num]=-1
		#print ("constructor is called")
        
	def freq(self,num,freq_dict):
		freq_dict2={}
		if num not in freq_dict:
			freq_dict2[num]=1
		else:
			freq_dict2[num]+=1
		return freq_dict2

	def ix_fun(self,freq_dict2,num):
		if(freq_dict2[num]==1):
			ix=0
		else:
			ix=freq_dict2[num]
		return ix

	def lx_fun(self,ind,arr,num,min_no,i):
		if (num==min_no):     # if in the array the num is minimum rank=1
			lx=0
		else:
			if(num==i and num!=0):
				lx=ind[i]
			else:
				lx=ind.index(i)
		return lx  

	def rank_fun(self,lx,ix):
		if(ix==0):
		    rank_num=lx
		else:
		    rank_num=lx+((1/ix)*(sum(range(1,(1+ix)))))
		    #print (rank_num)
		return rank_num
    
#	def __str__(self):
#		for key,value in sorted(self.rank_dict.items()):
#			return( "{} {} \n".format(self.key, self.value))

#def __str__(self):
#    c_list = 'Contact list\n' + '------------\n'
#    for key, value in sorted(self.d.items()):
#        c_list += str(Contact(key, value[0], value[1]))
#    return c_list
