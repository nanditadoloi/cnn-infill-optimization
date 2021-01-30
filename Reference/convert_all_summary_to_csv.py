from ecl.summary import EclSum
file_name = "/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/NEW_FILE_0.UNSMRY"
for i in range (500):
	part_1='/media/nandita/ND/Research/1_CNN_infill/spe10model2/SPE10 MODEL2 UPSCALED/data/NEW_FILE_'
	part_2='0'
	part_3='.UNSMRY'
	part_4='.csv'
	part_2=str(i)

	summary = EclSum(part_1+ part_2+ part_3)
	summary.export_csv(part_1+ part_2+ part_4)

	
	