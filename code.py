import netCDF4
from scipy.interpolate import interpn
## open text file containing the latitiude and longitude of the stations
file1=open(r"I:\data-precipitation\4-datasets\cordinates-station.txt")
for count,line in enumerate(file1):
	if count!=0:
		## iterate over all the time series netcdf file
		for file in glob.glob(r"I:\data-precipitation\4-datasets\cmorph\*.nc"):
			nc_file = netCDF4.Dataset(file,'r')
			print(file)
			## cmorph is the variable we are interested here, but can be anything like temperature
			temp = nc_file.variables['cmorph']
			# print(temp)
			lat = nc_file.variables['lat']
			lon = nc_file.variables['lon']
		# Define the point for which the data value is to be estimated, these assigns your location of the point of interest
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
			#since our point may not intersect at center of the grid exactly, so we did linear interpolationinterploate to derive the exact values
			point_temp = interpn((lats, lons), temps, (point_lat, point_lon), method='linear')

			# # Print the estimated temperature at the point
			# print(point_temp) this allows the time series value for single point and accordingly
			with open(r"I:\data-precipitation\4-datasets\cmorph\%s.txt"%(count),'a+') as f1:
				f1.write(str(round(point_temp[0],3))+'\n')
