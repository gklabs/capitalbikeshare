
import random
import scipy


class customer:
	def __init__(self,cust_id,cust_type,start_time, end_time,start_station_id,end_station_id, bikeid):
		self.cust_id= cust_id
		self.cust_type= cust_type
		self.start_time= start_time
		self.end_time= end_time
		self.start_station_id= start_station_id
		self.end_station_id= end_station_id
		self.bikeid = bikeid

class bike:
	def __init__(self,bikeid,biketype,status):
		self.bikeid= bikeid
		self.type= bike_type
		self.status= status

class station:
	def __init__(self,station_id,capacity,no_ebikes,no_pedalbikes, bike_list):
		self.station_id = station_id
		self.capacity = capacity
		self.no_ebikes = no_ebikes
		self.no_pedalbikes = no_pedalbikes
		self.bike_list= bike_list

	def UpdateNumberofBikes(self,option):


