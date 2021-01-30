
import numpy as np

x1=open('X-auxilary.csv','w')

def distance(pt_1, pt_2):
	dist=np.sqrt((pt_2[0]-pt_1[0])**2+(pt_2[1]-pt_1[1])**2)
	return dist

boundary_1=[1,1]
boundary_2=[15,1]
boundary_3=[15,55]
boundary_4=[1,55]
well=[7,27]



position_file = open('/media/nandita/ND/Research/1_CNN_infill/spe10model2/DataCollection/Testing/position_file.txt','r')
position_infil = position_file.readlines()
for i in position_infil:
	parts=i.split(';')
	xin=int(parts[0])-1
	yin=int(parts[1])-1
	infil_well=[xin,yin]
	dw1=distance(boundary_1,infil_well)
	dw2=distance(boundary_2,infil_well)
	dw3=distance(boundary_3,infil_well)
	dw4=distance(boundary_4,infil_well)
	dw5=distance(well,infil_well)
	
	x1.write(str(dw1) + ',' + str(dw2) + ',' + str(dw3) + ',' + str(dw4) + ',' + str(dw5))
	x1.write('\n')
	
x1.close()