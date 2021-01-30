
import numpy as np

x1=open('X-auxilary.csv','w')

def distance(pt_1, pt_2):
	dist=np.sqrt((pt_2[0]-pt_1[0])**2+(pt_2[1]-pt_1[1])**2)
	return dist

well_1=[1,1]
well_2=[15,1]
well_3=[15,55]
well_4=[1,55]
boundry=[15,55]



position_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/position_file.txt','r')
position_infil = position_file.readlines()
for i in position_infil:
	parts=i.split(';')
	xin=int(parts[0])
	yin=int(parts[1])
	infil_well=[xin,yin]
	dw1=distance(well_1,infil_well)
	dw2=distance(well_2,infil_well)
	dw3=distance(well_3,infil_well)
	dw4=distance(well_4,infil_well)
	dw5=distance(boundry,infil_well)
	
	x1.write(str(dw1) + ',' + str(dw2) + ',' + str(dw3) + ',' + str(dw4) + ',' + str(dw5))
	x1.write('\n')
	
x1.close()