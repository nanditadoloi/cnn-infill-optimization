import numpy as np
import matplotlib.pyplot as plt
porosity_file = open('interim_poro.txt','r')
data = porosity_file.readlines()
data= data[1:-1]
new_data = []
for i in data:
    new_data.append(float(i))
new_data = np.asarray(new_data).reshape(15,55,5, order="F")
plt.imshow(new_data[:,:,1],cmap='jet')
plt.colorbar()
plt.show()

x1=open('X-poro.txt','w')

w=5
position_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/position_file.txt','r')
position_infil = position_file.readlines()
for i in position_infil:
	parts=i.split(';')
	yin=int(parts[0])
	xin=int(parts[1])
	new_data_infil = new_data[xin-int(w/2):xin+int(w/2)+1 , yin-int(w/2):yin+int(w/2)+1 , :] ## Size of new_data_infill = w*w*5 = 5*5*5
	#new_data_infil=new_data[xin-1:xin+2,yin]
	for j in range(5):
		for k in range(5):
			for l in range(5):
				str(new_data_infil[j,k,l])
				x1.write(str(new_data_infil[j,k,l])+',')
	x1.write('\n')

x1.close()
