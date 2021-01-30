import numpy as np
interim_perm_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/interim_perm_.txt','r')
data = interim_perm_file.readlines()
data_permx=data[1:4126]
data_permy=data[4128:8253]
data_permz=data[8255:12380]
new_data_permx = []

x1=open('X-perm.txt','w')

for i in data_permx:
    new_data_permx.append(float(i))
new_data_permx = np.asarray(new_data_permx).reshape(15,55,5, order="F")
new_data_permy = []
for i in data_permy:
    new_data_permy.append(float(i))
new_data_permy = np.asarray(new_data_permy).reshape(15,55,5, order="F")
new_data_permz = []
for i in data_permz:
    new_data_permz.append(float(i))
new_data_permz = np.asarray(new_data_permz).reshape(15,55,5, order="F")


w=5
position_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/position_file.txt','r')
position_infil = position_file.readlines()
for i in position_infil:
	parts=i.split(';')
	yin=int(parts[0])
	xin=int(parts[1])
	new_data_infil_permx = new_data_permx[xin-int(w/2):xin+int(w/2)+1 , yin-int(w/2):yin+int(w/2)+1 , :]
	#new_data_infil_permx=new_data_permx[xin-1:xin+2,yin]
	for j in range(5):
		for k in range(5):
			for l in range(5):
				str(new_data_infil_permx[j,k,l])
				x1.write(str(new_data_infil_permx[j,k,l])+',')
	x1.write('\n')
	




w=5
position_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/position_file.txt','r')
position_infil = position_file.readlines()
for i in position_infil:
	parts=i.split(';')
	yin=int(parts[0])
	xin=int(parts[1])
	new_data_infil_permy = new_data_permy[xin-int(w/2):xin+int(w/2)+1 , yin-int(w/2):yin+int(w/2)+1 , :]
	#new_data_infil_permy=new_data_permy[xin-1:xin+2,yin]
	for j in range(5):
		for k in range(5):
			for l in range(5):
				str(new_data_infil_permy[j,k,l])
				x1.write(str(new_data_infil_permy[j,k,l])+',')
	x1.write('\n')
	




w=5
position_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/position_file.txt','r')
position_infil = position_file.readlines()
for i in position_infil:
	parts=i.split(';')
	yin=int(parts[0])
	xin=int(parts[1])
	new_data_infil_permz = new_data_permz[xin-int(w/2):xin+int(w/2)+1 , yin-int(w/2):yin+int(w/2)+1 , :]
	#new_data_infil_permz=new_data_permz[xin-1:xin+2,yin]
	for j in range(5):
		for k in range(5):
			for l in range(5):
				str(new_data_infil_permz[j,k,l])
				x1.write(str(new_data_infil_permz[j,k,l])+',')
	x1.write('\n')
	
x1.close()

	# print(new_data_infil_permz)
