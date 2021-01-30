import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
position_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/Training/data/position_file.txt','r')
position_infil = position_file.readlines()

x1=open('X-saturation_delete.csv','w')

w=5

for i in range(500):

	part_1='/media/nandita/ND/Research/1_CNN_infill/spe10model2/Training/data/NEW_FILE_'
	part_2='0'
	part_3='.csv'
	part_2=str(i)
	file_name=part_1+ part_2+ part_3
	df=pd.read_csv(file_name,sep=';')

	Heat_map=np.zeros((15,55,5))
	parts=position_infil[i].split(';')
	yin=int(parts[0])
	xin=int(parts[1])
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
			Heat_map[j,k,l] = value
	plt.imshow(Heat_map[:,:,2])
	plt.show()

	new_data_infil = Heat_map[xin-int(w/2):xin+int(w/2)+1 , yin-int(w/2):yin+int(w/2)+1 , :]

	for j in range(5):
		for k in range(5):
			for l in range(5):
				str(new_data_infil[j,k,l])
				x1.write(str(new_data_infil[j,k,l])+',')
	x1.write('\n')
	
x1.close()
	# print(new_data_infil)  
	# plt.imshow(Heat_map[:,:,0])
    # plt.show()



position_file.close()