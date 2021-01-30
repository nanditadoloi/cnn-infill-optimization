import numpy as np
porosity_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/DataCollection/Testing/interim_poro.txt','r')
data = porosity_file.readlines()
data= data[1:-1]
new_data = []
for i in data:
    new_data.append(float(i))
new_data = np.asarray(new_data).reshape(15,55,5, order="F")

x1=open('X-poro.csv','w')

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
