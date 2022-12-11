import netCDF4
from scipy.interpolate import interpn
file1=open(r"I:\data-precipitation\4-datasets\cordinates-station.txt")
for count,line in enumerate(file1):
	if count!=0:
		for file in glob.glob(r"I:\data-precipitation\4-datasets\cmorph\*.nc"):
			nc_file = netCDF4.Dataset(file,'r')
			print(file)

			temp = nc_file.variables['cmorph']
			# print(temp)
			lat = nc_file.variables['lat']
			lon = nc_file.variables['lon']
		# Define the point for which the data value is to be estimated
			point_lat = line.split('\t')[1]
			point_lon = line.split('\t')[2]
			# Define the coordinates of the data grid
			lats = lat[:]
			# print(lats)
			lons = lon[:]
			# print(lons)
			# Define the data values of the data grid
			temps = temp[0,:,:]
			# print(temps)
			# Estimate the temperature at the specified point using linear interpolation
			point_temp = interpn((lats, lons), temps, (point_lat, point_lon), method='linear')

			# # Print the estimated temperature at the point
			# print(point_temp)
			with open(r"I:\data-precipitation\4-datasets\cmorph\%s.txt"%(count),'a+') as f1:
				f1.write(str(round(point_temp[0],3))+'\n')
