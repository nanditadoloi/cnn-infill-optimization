import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_name= 'PAPER_INITIAL_10.csv'
df=pd.read_csv(file_name,sep=';')
new_data=np.zeros((15,55,5))



for j in range(15):
    for k in range(55):
        for l in range(5):
            part_1='BPR:'
            part_2=str(j+1)
            part_3=','+str(k+1)
            part_4=','+str(l+1)
            layer_name=part_1+ part_2+ part_3+part_4
            data = df[layer_name]
            value = data.to_numpy()[-1]
            new_data[j,k,l] = value


plt.imshow(new_data[:,:,1],cmap='jet',vmin=4120,vmax=np.max(new_data[:,:,1])*1.)
plt.colorbar()
plt.show()

x1=open('X-pressure.csv','w')


for j in range(15):
	for k in range(55):
		for l in range(5):
			x1.write(str(new_data[j,k,l])+',')
x1.write('\n')

x1.close()
