import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

y1=open('Y-FOPT.csv','w')


for i in range(500):

	part_1='/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/NEW_FILE_'
	part_2='0'
	part_3='.csv'
	part_2=str(i)
	file_name=part_1+ part_2+ part_3
	df=pd.read_csv(file_name,sep=';')

	data = df['FOPT']
	value = data.to_numpy()[-1]

	y1.write(str(value) +',')
	y1.write('\n')
	
y1.close()

# print(y)	