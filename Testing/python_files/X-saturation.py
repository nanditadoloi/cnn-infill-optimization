import numpy as np
import pandas as pd
file_name= '/media/nandita/ND/Research/1_CNN_infill/spe10model2/DataCollection/Testing/PAPER_INITIAL_10.csv'
df=pd.read_csv(file_name,sep=';')

new_data=np.zeros((15,55,5))
for j in range(15):	  
  for k in range(55):
  	for l in range(5):
  		part_1='BOSAT:'
		part_2=str(j+1)
		part_3=','+str(k+1)
		part_4=','+str(l+1)
		layer_name=part_1+ part_2+ part_3+part_4
		data = df[layer_name]
		value = data.to_numpy()[-1]
		new_data[j,k,l] = value

x1=open('X-saturation.csv','w')

w=5
position_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/DataCollection/Testing/position_file.txt','r')
position_infil = position_file.readlines()
for i in position_infil:
	parts=i.split(';')
	yin=int(parts[0])-1
	xin=int(parts[1])-1
	new_data_infil = new_data[xin-int(w/2):xin+int(w/2)+1 , yin-int(w/2):yin+int(w/2)+1 , :] ## Size of new_data_infill = w*w*5 = 5*5*5
	#new_data_infil=new_data[xin-1:xin+2,yin]
	for j in range(5):
		for k in range(5):
			for l in range(5):
				str(new_data_infil[j,k,l])
				x1.write(str(new_data_infil[j,k,l])+',')
	x1.write('\n')
	
x1.close()











