import numpy as np
import os

template_file = open('PAPER_INITIAL_10_RESTART_TEMPLATE.DATA','r')
data = template_file.read()
template_file.close()
position_file=open('position_file.txt','w')

i=0

for iw in range(3,54):
	for jw in range(3,14):
		r1 = str(iw)
		r2 = str(jw)
		
		new_data = data.replace('D2', r1)
		new_data = new_data.replace('DPM', r2)
		position_file.write(r1 +';'+r2 + '\n')

	    

		file_name = 'new_file_'+ str(i) +'.data' 
		new_file = open(file_name,'w')
		new_file.write(new_data)
		new_file.close()

		os.system("mpirun -np 4 flow " + file_name)
		i=i+1

position_file.close()
