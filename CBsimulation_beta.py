
import random
import numpy as np
import scipy
import bisect
import pandas as pd
import matplotlib.pyplot as plt



class customer:
	def __init__(self,cust_id,system,cust_type,bike,start_time, end_time,duration,perm_start_station_id,start_station_id,end_station_id,satisfaction ):
		self.cust_id= cust_id
		self.system= system
		self.cust_type= cust_type
		self.bike = bike #assigns the bike object to the customer
		self.start_time= start_time
		self.end_time= end_time
		self.duration=duration
		self.perm_start_station_id = perm_start_station_id
		self.start_station_id= start_station_id
		self.end_station_id= end_station_id
		self.satisfaction = satisfaction #0 means satisfied, 1 means dissatisfied
		
	def giveinfo(self):
		print(self.cust_id,
		self.system,
		self.cust_type,
		self.bike.bike_type,
		self.start_time,
		self.end_time,
		self.duration,
		self.perm_start_station_id ,
		self.start_station_id,
		self.end_station_id,
		self.satisfaction)	

class bike:
	def __init__(self,bikeid,station_id,bike_type,status):
		self.bikeid= bikeid
		self.current_station= station_id
		self.bike_type= bike_type
		self.status= status

class station:
	def __init__(self,station_id,capacity,no_empty_docks,no_ebikes,no_pedalbikes, bike_list):
		self.station_id = station_id
		self.capacity = capacity
		self.no_empty_docks = no_empty_docks
		self.no_ebikes = no_ebikes
		self.no_pedalbikes = no_pedalbikes
		self.bike_list= bike_list

	def UpdateNumberofBikes(self,biketype_assigned,kind):

		# print("updating the bikes in the station")

		if kind == "pickup" :
			self.no_empty_docks+=1
			if biketype_assigned=="pedalbike":
				self.no_pedalbikes-=1
			else:
				self.no_ebikes-=1
			
		#removing bike from the station's bikelist is done in give_bike function
		elif(self.no_empty_docks <= self.capacity): #return a bike
			self.no_empty_docks-=1
			if biketype_assigned=="pedalbike":
				self.no_pedalbikes+=1

			else:
				self.no_ebikes+=1


def give_start_station(system):
	#assign customer to  start station and end station based on priors
	cust_start_node = random.uniform(0,1)
	if PROPOSED_STATION:
		cust_start_node_cdf = [0.1504,0.2847,0.4269,0.5835,0.6847,0.8847,1.0000]
	else:
		cust_start_node_cdf = [0.162753,0.338462,0.507693,0.689070,0.800811,1]
	if PROPOSED_STATION:
		if (system == "in_system"):
			if cust_start_node <=cust_start_node_cdf[0]:
				start_station_id= 31104
			elif cust_start_node > cust_start_node_cdf[0] and cust_start_node <= cust_start_node_cdf[1] :
				start_station_id= 31110
			elif cust_start_node > cust_start_node_cdf[1] and cust_start_node <= cust_start_node_cdf[2] :
				start_station_id= 31113
			elif cust_start_node > cust_start_node_cdf[2] and cust_start_node <= cust_start_node_cdf[3] :
				start_station_id= 31114
			elif cust_start_node > cust_start_node_cdf[3] and cust_start_node <= cust_start_node_cdf[4] :
				start_station_id= 31116
			elif cust_start_node > cust_start_node_cdf[4] and cust_start_node <= cust_start_node_cdf[5] :
				start_station_id= 31296
			elif cust_start_node > cust_start_node_cdf[5] and cust_start_node <= cust_start_node_cdf[6] :
				start_station_id= 40000
		elif(system == "in_out"):
			cust_start_node_cdf = [0.1645,0.3415,0.4402,0.6003,0.7217,0.8817,1.0000]
			if cust_start_node <=cust_start_node_cdf[0]:
				start_station_id= 31104
			elif cust_start_node > cust_start_node_cdf[0] and cust_start_node <= cust_start_node_cdf[1] :
				start_station_id= 31110
			elif cust_start_node > cust_start_node_cdf[1] and cust_start_node <= cust_start_node_cdf[2] :
				start_station_id= 31113
			elif cust_start_node > cust_start_node_cdf[2] and cust_start_node <= cust_start_node_cdf[3] :
				start_station_id= 31114
			elif cust_start_node > cust_start_node_cdf[3] and cust_start_node <= cust_start_node_cdf[4] :
				start_station_id= 31116
			elif cust_start_node > cust_start_node_cdf[4] and cust_start_node <= cust_start_node_cdf[5] :
				start_station_id= 31296
			elif cust_start_node > cust_start_node_cdf[5] and cust_start_node <= cust_start_node_cdf[6] :
				start_station_id= 40000
	else:
		if (system == "in_system"):

			if cust_start_node <=cust_start_node_cdf[0]:
				start_station_id= 31104
			elif cust_start_node > cust_start_node_cdf[0] and cust_start_node <= cust_start_node_cdf[1] :
				start_station_id= 31110
			elif cust_start_node > cust_start_node_cdf[1] and cust_start_node <= cust_start_node_cdf[2] :
				start_station_id= 31113
			elif cust_start_node > cust_start_node_cdf[2] and cust_start_node <= cust_start_node_cdf[3] :
				start_station_id= 31114
			elif cust_start_node > cust_start_node_cdf[3] and cust_start_node <= cust_start_node_cdf[4] :
				start_station_id= 31116
			elif cust_start_node > cust_start_node_cdf[4] and cust_start_node <= cust_start_node_cdf[5] :
				start_station_id= 31296
		elif(system == "in_out"):
			cust_start_node_cdf = [0.175851,0.399058,0.524514,0.70776,0.839395,1]
			if cust_start_node <=cust_start_node_cdf[0]:
				start_station_id= 31104
			elif cust_start_node > cust_start_node_cdf[0] and cust_start_node <= cust_start_node_cdf[1] :
				start_station_id= 31110
			elif cust_start_node > cust_start_node_cdf[1] and cust_start_node <= cust_start_node_cdf[2] :
				start_station_id= 31113
			elif cust_start_node > cust_start_node_cdf[2] and cust_start_node <= cust_start_node_cdf[3] :
				start_station_id= 31114
			elif cust_start_node > cust_start_node_cdf[3] and cust_start_node <= cust_start_node_cdf[4] :
				start_station_id= 31116
			elif cust_start_node > cust_start_node_cdf[4] and cust_start_node <= cust_start_node_cdf[5] :
				start_station_id= 31296

	return start_station_id

def give_end_station(start_station_id,system):
	cust_end_node = random.uniform(0,1)

	if PROPOSED_STATION:
			station_ids = [31104,31110,31113,31114,31116,31296,40000]
			end_station_joint_dist = np.array([[0.0713,0.2021,0.0713,0.1585,0.1863,	0.1070,	0.2034],[0.1181,0.1105,	0.0686,	0.2210,	0.0991,	0.2096,	0.1731], [0.0589,0.2819,0.0883,	0.1388,	0.1262,	0.1851,	0.1207],[0.1629,0.3009,	0.0389,	0.0814,	0.0354,	0.1735,	0.2069],[0.1874,0.1932,	0.0878,	0.0820,	0.0703,	0.1874,	0.1919],[0.1003,0.2251,	0.1626,	0.1592,	0.1176,	0.0864,	0.1487],[0.1648,0.1402,	0.0978,	0.1676,	0.1554,	0.1205,	0.1537]])
	else:
		station_ids = [31104,31110,31113,31114,31116,31296]
		end_station_joint_dist = np.array([[0.089562,0.253732,0.089552,0.199005,0.233831,0.134328],[0.142857,0.133641,0.082949,0.267281,0.119816,0.253456],[0.066986,0.320574,0.100478,0.157895,0.143541,0.210526],[0.205357,0.379464,0.049107,0.102679,0.044643,0.218750],[0.231884,0.239130,0.108696,0.101449,0.086957,0.231884],[0.117887,0.26442,0.191057,0.186992,0.138211,0.101525]])
	
	
		
	

	if PROPOSED_STATION:
		if (system=="in_system"):
			end_index= station_ids.index(start_station_id)
			end_station_id =0

			cust_end_node_cdf_temp= end_station_joint_dist[end_index]
			cust_end_node_cdf =[]
			y=x=0
			for x in cust_end_node_cdf_temp:
				y=y+x
				cust_end_node_cdf.append(y)
			
			if cust_end_node <=cust_end_node_cdf[0]:
				end_station_id= 31104
			elif cust_end_node > cust_end_node_cdf[0] and cust_end_node <= cust_end_node_cdf[1]:
				end_station_id= 31110
			elif cust_end_node > cust_end_node_cdf[1] and cust_end_node <= cust_end_node_cdf[2]:
				end_station_id= 31113
			elif cust_end_node > cust_end_node_cdf[2] and cust_end_node <= cust_end_node_cdf[3]:
				end_station_id= 31114
			elif cust_end_node > cust_end_node_cdf[3] and cust_end_node <= cust_end_node_cdf[4]:
				end_station_id= 31116
			elif cust_end_node > cust_end_node_cdf[4] and cust_end_node <= cust_end_node_cdf[5]:
				end_station_id= 31296
			elif cust_end_node > cust_end_node_cdf[5] and cust_end_node <= cust_end_node_cdf[6]:
				end_station_id= 40000
			# print("end station_id is {}".format(end_station_id))
		
		elif(system=="out_in"):
			cust_end_node_cdf = [0.1643, 0.3886,0.4610,0.6183,0.7684,0.8832,1.0000]
			if cust_end_node <=cust_end_node_cdf[0]:
					end_station_id= 31104
			elif cust_end_node > cust_end_node_cdf[0] and cust_end_node <= cust_end_node_cdf[1]:
				end_station_id= 31110
			elif cust_end_node > cust_end_node_cdf[1] and cust_end_node <= cust_end_node_cdf[2]:
				end_station_id= 31113
			elif cust_end_node > cust_end_node_cdf[2] and cust_end_node <= cust_end_node_cdf[3]:
				end_station_id= 31114
			elif cust_end_node > cust_end_node_cdf[3] and cust_end_node <= cust_end_node_cdf[4]:
				end_station_id= 31116
			elif cust_end_node > cust_end_node_cdf[4] and cust_end_node <= cust_end_node_cdf[5]:
				end_station_id= 31296
			elif cust_end_node > cust_end_node_cdf[5] and cust_end_node <= cust_end_node_cdf[6]:
				end_station_id= 40000

	else:

		if (system=="in_system"):
			end_index= station_ids.index(start_station_id)
			end_station_id =0

			cust_end_node_cdf_temp= end_station_joint_dist[end_index]
			cust_end_node_cdf =[]
			y=x=0
			for x in cust_end_node_cdf_temp:
				y=y+x
				cust_end_node_cdf.append(y)
			
			if cust_end_node <=cust_end_node_cdf[0]:
					end_station_id= 31104
			elif cust_end_node > cust_end_node_cdf[0] and cust_end_node <= cust_end_node_cdf[1]:
				end_station_id= 31110
			elif cust_end_node > cust_end_node_cdf[1] and cust_end_node <= cust_end_node_cdf[2]:
				end_station_id= 31113
			elif cust_end_node > cust_end_node_cdf[2] and cust_end_node <= cust_end_node_cdf[3]:
				end_station_id= 31114
			elif cust_end_node > cust_end_node_cdf[3] and cust_end_node <= cust_end_node_cdf[4]:
				end_station_id= 31116
			elif cust_end_node > cust_end_node_cdf[4] and cust_end_node <= cust_end_node_cdf[5]:
				end_station_id= 31296
			# print("end station_id is {}".format(end_station_id))
		
		elif(system=="out_in"):
			cust_end_node_cdf = [0.18627,0.441064,0.52293,0.700426,0.869928,1]
			if cust_end_node <=cust_end_node_cdf[0]:
					end_station_id= 31104
			elif cust_end_node > cust_end_node_cdf[0] and cust_end_node <= cust_end_node_cdf[1]:
				end_station_id= 31110
			elif cust_end_node > cust_end_node_cdf[1] and cust_end_node <= cust_end_node_cdf[2]:
				end_station_id= 31113
			elif cust_end_node > cust_end_node_cdf[2] and cust_end_node <= cust_end_node_cdf[3]:
				end_station_id= 31114
			elif cust_end_node > cust_end_node_cdf[3] and cust_end_node <= cust_end_node_cdf[4]:
				end_station_id= 31116
			elif cust_end_node > cust_end_node_cdf[4] and cust_end_node <= cust_end_node_cdf[5]:
				end_station_id= 31296
			# print("end station_id is {}".format(end_station_id))
	return end_station_id

# This function gives the duration based on bike type, the start and end stations
def give_duration(station_ids,bike_type,start_station_id,end_station_id):
	
	start_index= station_ids.index(start_station_id)
	end_index = station_ids.index(end_station_id)

	##### reading duration from the csv file
	if PROPOSED_STATION:
		ebike_data= pd.read_csv("ebikepiv_proposed.csv")
		pedalbike_data= pd.read_csv("pedalpiv_proposed.csv")
		
	else:	
		ebike_data= pd.read_csv("ebikepiv.csv")
		pedalbike_data= pd.read_csv("pedalpiv.csv")


	# print(ebike_data)
	# print(pedalbike_data)
	for c in ebike_data.columns[1:]:
		ebike_data[c] = [truncate(x/60) for x in ebike_data[c]]
	for c in pedalbike_data.columns[1:]:
		pedalbike_data[c] = [truncate(x/60) for x in pedalbike_data[c]]
	#print("after \n ", ebike_data)
	#print("after \n ", pedalbike_data)
	ebike_duration_matrix = ebike_data.loc[:, ebike_data.columns != 'startnode'].values
	pedal_duration_matrix = pedalbike_data.loc[:, pedalbike_data.columns != 'startnode'].values


	if bike_type == "pedalbike":
		return pedal_duration_matrix[start_index][end_index]
	else:
		return ebike_duration_matrix[start_index][end_index]

def give_bike(stations_list,start_station_id,pref_bike):

	# check if preferred bike exists in start station
	for x in stations_list:
		if start_station_id == x.station_id:
			station_index= stations_list.index(x)
			break
	
	if pref_bike == "ebike":
		if stations_list[station_index].no_ebikes > 0 and len(stations_list[station_index].bike_list)>0:
			flag=1
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="ebike":
					stations_list[station_index].bike_list.remove(y)
					stations_list[station_index].UpdateNumberofBikes(y.bike_type,"pickup")
					# stations_list[station_index].no_ebikes-=1
					# stations_list[station_index].no_empty_docks+= 1
					y.status="riding"
					return y
			
		else: #try to assign pedal bike if ebike is unavailable
			if stations_list[station_index].no_pedalbikes > 0 and len(stations_list[station_index].bike_list)>0:
				flag=0
				for y in stations_list[station_index].bike_list:
					if y.bike_type=="pedalbike":
						stations_list[station_index].bike_list.remove(y)
						stations_list[station_index].UpdateNumberofBikes(y.bike_type,"pickup")
						# stations_list[station_index].no_pedalbikes-=1
						# stations_list[station_index].no_empty_docks+= 1
						
						y.status="riding"
						return y
			else:
				# print("no bikes available. Bike not assigned")
				return None
	else: # preferred bike is pedal bike
		if stations_list[station_index].no_pedalbikes >0 and len(stations_list[station_index].bike_list)>0:
			flag=1
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="pedalbike":
					stations_list[station_index].bike_list.remove(y)
					stations_list[station_index].UpdateNumberofBikes(y.bike_type,"pickup")
					# stations_list[station_index].no_pedalbikes-=1
					# stations_list[station_index].no_empty_docks+= 1
					y.status="riding"
					return y
		else:
			if stations_list[station_index].no_ebikes > 0 and len(stations_list[station_index].bike_list)>0:
				flag=0
				for y in stations_list[station_index].bike_list:
					if y.bike_type=="ebike":
						stations_list[station_index].bike_list.remove(y)
						stations_list[station_index].UpdateNumberofBikes(y.bike_type,"pickup")
						# stations_list[station_index].no_ebikes-=1
						# stations_list[station_index].no_empty_docks+= 1
						y.status="riding"
						return y
			else:
				# print("no bikes available. Bike not assigned")
				return None
def truncate(n, decimals=0):
	multiplier = 10 ** decimals
	return int(n * multiplier) / multiplier
#===============================================================

#implementing thinning algorithm
def give_arrivals(PROPOSED_STATION):
	if PROPOSED_STATION == True:
		vhrthin = pd.read_csv("thinningdata.csv")
		dfoos = pd.read_csv("oos_newnode.csv")
		# variable inputs
		SEED = None
		MAXSEEDSEQ = 100000
		u1count = 0
		counter = 0

		inc_rate = 1.10
		vhrthin['perhr'] = vhrthin.perhr*inc_rate
		## thin based on new node
		## generate ALL t* under maxlambda in 24 hr period and then thin
		maxlambda = np.max(vhrthin.perhr)+.3
		# print("max lambda: ", maxlambda)
		#generate first customer arrival
		u1 = random.uniform(0,1)
		lambda0 = vhrthin.loc[vhrthin.index == 0, 'perhr'].iloc[0]
		cust1 = -1/lambda0*np.log(u1)
		vtime = cust1
		cust_total = []
		cust_total.append(vtime)
		while vtime < 24:
			u1 = random.uniform(0,1)
			vtime = vtime - (1/maxlambda)*np.log(u1)
			cust_total.append(vtime)
			if len(cust_total) > 1000: 
				break
		cust_total.pop(-1) #pop inplace=True by default
		cust_ftotal = []
		customer_startinendin = []
		ncust = 1
		#thin arrival times here
		for x in range(len(cust_total)):
			u2 = random.uniform(0,1)
			tlambda = np.floor(cust_total[x])
			tlambda = vhrthin.loc[vhrthin.hr == tlambda,'perhr'].iloc[0]
			if u2 <= tlambda / maxlambda:
				cust_ftotal.append(cust_total[x])
				customer_startinendin.append((ncust, cust_total[x]))
				ncust +=1

		'''
		##print list
		cust_ftotal = pd.DataFrame(cust_ftotal)
		cust_ftotal.columns = ["arrival_time"]
		cust_ftotal['arrhour'] = cust_ftotal.arrival_time.apply(lambda x: np.floor(x))
		cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))
		(cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))).sum()
		'''
		## arrival times for those that start IN network but end OUTSIDE network [start,end)
		
		## generate ALL t* under maxlambda in 24 hr period and then thin
		maxlambda = np.max(dfoos.startinendout_lambda)
		#generate first customer arrival
		u1 = random.uniform(0,1)
		lambda0 = dfoos.loc[dfoos.index == 0, 'startinendout_lambda'].iloc[0]
		cust1 = -1/lambda0*np.log(u1)
		vtime = cust1
		cust_total = []
		cust_total.append(vtime)
		while vtime < 24:
			u1 = random.uniform(0,1)
			vtime = vtime - (1/maxlambda)*np.log(u1)
			cust_total.append(vtime)
			if len(cust_total) > 1000: 
				break

		cust_total.pop(-1) #pop inplace=True by default
		len(cust_total)
		cust_ftotal = []
		customer_startinendout = []
		ncust = 1
		#thin arrival times here
		for x in range(len(cust_total)):
			u2 = random.uniform(0,1)
			tlambda = np.floor(cust_total[x])
			tlambda = dfoos.loc[dfoos.hour == tlambda,'startinendout_lambda'].iloc[0]
			if u2 <= tlambda / maxlambda:
				cust_ftotal.append(cust_total[x])
				customer_startinendout.append((ncust, cust_total[x]))
				ncust +=1

		cust_ftotal = pd.DataFrame(cust_ftotal)
		cust_ftotal.columns = ["arrival_time"]
		cust_ftotal['arrhour'] = cust_ftotal.arrival_time.apply(lambda x: np.floor(x))

		##print list
		cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))
		(cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))).sum()

		## arrival times for those that start OUT network but end INSIDE network (start,end]
		## generate ALL t* under maxlambda in 24 hr period and then thin
		maxlambda = np.max(dfoos.startoutendin_lambda)
		#generate first customer arrival
		u1 = random.uniform(0,1)
		lambda0 = dfoos.loc[dfoos.index == 0, 'startoutendin_lambda'].iloc[0]
		cust1 = -1/lambda0*np.log(u1)
		vtime = cust1
		cust_total = []
		cust_total.append(vtime)

		while vtime < 24:
			u1 = random.uniform(0,1)
			vtime = vtime - (1/maxlambda)*np.log(u1)
			cust_total.append(vtime)
			if len(cust_total) > 1000: 
				break
		cust_total.pop(-1) #pop inplace=True by default
		len(cust_total)
		cust_ftotal = []
		customer_startoutendin = []
		ncust = 1

		#thin arrival times here
		for x in range(len(cust_total)):
			u2 = random.uniform(0,1)
			tlambda = np.floor(cust_total[x])
			tlambda = dfoos.loc[dfoos.hour == tlambda,'startoutendin_lambda'].iloc[0]
			if u2 <= tlambda / maxlambda:
				cust_ftotal.append(cust_total[x])
				customer_startoutendin.append((ncust, cust_total[x]))
				ncust +=1

		cust_ftotal = pd.DataFrame(cust_ftotal)
		cust_ftotal.columns = ["arrival_time"]
		cust_ftotal['arrhour'] = cust_ftotal.arrival_time.apply(lambda x: np.floor(x))

		##print list
		cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))
		(cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))).sum()

		
	else:
		# variable inputs
		SEED = None
		counter = 0
		# *** OUTPUT: customer_times[] contains customer arrival times tuple (customer #, arrival time (hr))
		## code below
		random.seed(SEED)
		vhrthin = pd.read_csv("thinningdata.csv")
		dfoos = pd.read_csv("outofsystems.csv")
		## with original thinning algo
		maxlambda = np.max(vhrthin.perhr)+.3
		# print("max lambda: ", maxlambda)
		#generate first customer arrival
		u1 = random.uniform(0,1)
		lambda0 = vhrthin.loc[vhrthin.index == 0, 'perhr'].iloc[0]
		cust1 = -1/lambda0*np.log(u1)
		vtime = cust1
		cust_total = []
		cust_total.append(vtime)
		while vtime < 24:
			u1 = random.uniform(0,1)
			vtime = vtime - (1/maxlambda)*np.log(u1)
			cust_total.append(vtime)
			if len(cust_total) > 1000: 
				break

		cust_total.pop(-1) #pop inplace=True by default
		cust_ftotal = []
		customer_startinendin = []
		ncust = 1
		#thin arrival times here
		for x in range(len(cust_total)):
			u2 = random.uniform(0,1)
			tlambda = np.floor(cust_total[x])
			tlambda = vhrthin.loc[vhrthin.hr == tlambda,'perhr'].iloc[0]
			if u2 <= tlambda / maxlambda:
				cust_ftotal.append(cust_total[x])
				customer_startinendin.append((ncust, cust_total[x]))
				ncust +=1

		'''
		##print list
		cust_ftotal = pd.DataFrame(cust_ftotal)
		cust_ftotal.columns = ["arrival_time"]
		cust_ftotal['arrhour'] = cust_ftotal.arrival_time.apply(lambda x: np.floor(x))
		cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))
		(cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))).sum()
		'''

		#=============================================
		## generate ALL t* under maxlambda in 24 hr period and then thin
		maxlambda = np.max(dfoos.startinendout_lambda)
		#generate first customer arrival
		u1 = random.uniform(0,1)
		lambda0 = dfoos.loc[dfoos.index == 0, 'startinendout_lambda'].iloc[0]
		cust1 = -1/lambda0*np.log(u1)
		vtime = cust1
		cust_total = []
		cust_total.append(vtime)
		while vtime < 24:
			u1 = random.uniform(0,1)
			vtime = vtime - (1/maxlambda)*np.log(u1)
			cust_total.append(vtime)
			if len(cust_total) > 1000: 
				break

		cust_total.pop(-1) #pop inplace=True by default
		len(cust_total)
		cust_ftotal = []
		customer_startinendout = []
		ncust = 1

		#thin arrival times here
		for x in range(len(cust_total)):
			u2 = random.uniform(0,1)
			tlambda = np.floor(cust_total[x])
			tlambda = dfoos.loc[dfoos.hour == tlambda,'startinendout_lambda'].iloc[0]
			if u2 <= tlambda / maxlambda:
				cust_ftotal.append(cust_total[x])
				customer_startinendout.append((ncust, cust_total[x]))
				ncust +=1

		cust_ftotal = pd.DataFrame(cust_ftotal)
		cust_ftotal.columns = ["arrival_time"]
		cust_ftotal['arrhour'] = cust_ftotal.arrival_time.apply(lambda x: np.floor(x))

		##print list
		cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))
		(cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))).sum()

		# print(customer_startoutendin)
		######################################################
		## arrival times for those that start OUT network but end INSIDE network (start,end]

		## generate ALL t* under maxlambda in 24 hr period and then thin
		maxlambda = np.max(dfoos.startoutendin_lambda)
		#generate first customer arrival
		u1 = random.uniform(0,1)
		lambda0 = dfoos.loc[dfoos.index == 0, 'startoutendin_lambda'].iloc[0]
		cust1 = -1/lambda0*np.log(u1)
		vtime = cust1
		cust_total = []
		cust_total.append(vtime)

		while vtime < 24:
			u1 = random.uniform(0,1)
			vtime = vtime - (1/maxlambda)*np.log(u1)
			cust_total.append(vtime)
			if len(cust_total) > 1000: 
				break

		cust_total.pop(-1) #pop inplace=True by default
		len(cust_total)
		cust_ftotal = []
		customer_startoutendin = []
		ncust = 1
		#thin arrival times here
		for x in range(len(cust_total)):
			u2 = random.uniform(0,1)
			tlambda = np.floor(cust_total[x])
			tlambda = dfoos.loc[dfoos.hour == tlambda,'startoutendin_lambda'].iloc[0]
			if u2 <= tlambda / maxlambda:
				cust_ftotal.append(cust_total[x])
				customer_startoutendin.append((ncust, cust_total[x]))
				ncust +=1

		cust_ftotal = pd.DataFrame(cust_ftotal)
		cust_ftotal.columns = ["arrival_time"]
		cust_ftotal['arrhour'] = cust_ftotal.arrival_time.apply(lambda x: np.floor(x))

		##print list
		cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))
		(cust_ftotal.groupby('arrhour').agg(vcount = ('arrhour','count'))).sum()

		
		# print("in sys {} start in and end out {} start out end in {}".format(len(customer_times),len(customer_startinendout), len(customer_startoutendin)))
	return customer_startinendin, customer_startinendout,customer_startoutendin

	
	###################################################
def give_customers(t,arrival_times):

	no_cust_at_time= 0
	for time in arrival_times:
		if time == t:
			no_cust_at_time+=1

	return no_cust_at_time

#===============================================================

def return_bike(station_ids,stations_list,nearest_node,t,cust):
	for s in stations_list:
				if s.station_id==cust.end_station_id:
					if s.no_empty_docks !=0:
						# print("empty dock available to return")
						s.bike_list.append(cust.bike)
						cust.bike.current_station=s.station_id
						cust.bike.status= "stationary"
						s.UpdateNumberofBikes(cust.bike.bike_type, "return")
						# end_trip_customer.remove(cust)

					else:
						# print("no empty dock available, redirecting to another station")
						for ids in station_ids:
							if cust.end_station_id==ids:
								#start station must be the initial end station
								cust.start_station_id=cust.end_station_id
								#assign the next station from the list as end station
								cust.end_station_id = nearest_node[cust.end_station_id]
								#change duration
								cust.duration= give_duration(station_ids,cust.bike.bike_type,cust.start_station_id,cust.end_station_id)
								cust.end_time= t + cust.duration
								cust.satisfaction=1

def print_station(stations_list):
	# print("station resources")
	for x in stations_list:
		print("=========================")
		print("station id {} \n Capacity {}\n no_ebikes {} \n no_pedalbikes {} \n no_emptydocks {}".format( x.station_id, x.capacity,x.no_ebikes,x.no_pedalbikes,x.no_empty_docks))
		

def print_metrics(run,customer_list,kickedout_cust):
	diss_bike=0
	diss_return=0
	metrics_tuple =()
	duration=[]
	revenue =pedalbike_count=ebike_count=member_count=casual_count=0
	ecoloss=0
	for x in customer_list:
		if x.cust_type == "member":
			member_count+=1
		else:
			casual_count+=1
		if x.bike.bike_type == "ebike":
			revenue+=3
			ebike_count+=1
		else:
			revenue+=2
			pedalbike_count+=1

		if(x.satisfaction== 2):
			diss_bike+=1
		elif(x.satisfaction==1):
			diss_return+=1
	print("no customers who could not get the bike of choice {} ".format(diss_bike))
	print("no customers who could not return bike at intended station {} ".format(diss_return))
	for x in kickedout_cust:
		if x.bike.bike_type=="pedalbike":
			ecoloss+= 2
		else:
			ecoloss+= 3
	biketypeutil_ebike = ebike_count/len(customer_list)
	biketypeutil_pedalbike = pedalbike_count/len(customer_list)
	mem_util = member_count/len(customer_list)
	casual_util= casual_count/len(customer_list)

	succ_cust= len(customer_list)
	fail_cust = len(kickedout_cust)

	metrics_tuple = (run,succ_cust,fail_cust,diss_bike,diss_return,revenue,ecoloss,biketypeutil_ebike,biketypeutil_pedalbike,mem_util,casual_util)
	# print("Revenue: {}\n Economic Loss {}".format(revenue,ecoloss))
	return metrics_tuple
			

#==============================================================================
def give_cust_type():
	# casual vs member (0.2810 vs 0.7189)
	casual_member= random.uniform(0,1)
	if casual_member>= 0.718929:
		cust_type= "casual"
	else:
		cust_type ="member"
	return cust_type

def give_bike_type():
	pedal_ebike= random.uniform(0,1)
	if pedal_ebike>= 0.881335:
		pref_bike= "pedalbike"
	else:
		pref_bike ="ebike"
	return pref_bike

def create_dataset(run,customer_list,kickedout_customer):
	moved_out_data = pd.DataFrame(columns= ["run","cust_id","system","cust_type","bike_type","start_time", "end_time","duration","perm_start_station_id","start_station_id","end_station_id","satisfaction"])
	sim_data = pd.DataFrame(columns= ["run","cust_id","system","cust_type","bike_type","start_time", "end_time","duration","perm_start_station_id","start_station_id","end_station_id","satisfaction"])
	
	for x in customer_list:
		sim_data = sim_data.append({"run":run,"cust_id":x.cust_id,"system":x.system,"cust_type":x.cust_type,"bike_type":x.bike.bike_type,"start_time": x.start_time, "end_time": x.end_time,"duration": x.duration,"perm_start_station_id": x.perm_start_station_id,"start_station_id":x.start_station_id,"end_station_id":x.end_station_id,"satisfaction":x.satisfaction}, ignore_index=True)

	for y in kickedout_customer:
		moved_out_data = moved_out_data.append({"run":run,"cust_id":y.cust_id,"system":y.system,"cust_type":y.cust_type,"bike_type":y.bike.bike_type,"start_time": y.start_time, "end_time": y.end_time,"duration": y.duration,"perm_start_station_id": y.perm_start_station_id,"start_station_id":y.start_station_id,"end_station_id":y.end_station_id,"satisfaction":y.satisfaction},  ignore_index=True)
	
	full_sim_data = pd.concat([sim_data,moved_out_data])
	succ_start_station_count = pd.DataFrame(sim_data.perm_start_station_id.value_counts())
	succ_end_station_count = pd.DataFrame(sim_data.end_station_id.value_counts())
	
	fail_start_station_count = pd.DataFrame(moved_out_data.perm_start_station_id.value_counts())
	fail_end_station_count = pd.DataFrame(moved_out_data.end_station_id.value_counts())
	
	# print(succ_start_station_count)
	# print(succ_end_station_count)
	# print(fail_start_station_count)
	# print(fail_end_station_count)


	dfs = [succ_start_station_count, succ_end_station_count,fail_start_station_count, fail_end_station_count] 
	nan_value = 0 
	# solution 1 (fast) 
	dock_util = pd.concat(dfs, join='outer', axis=1).fillna(nan_value)
	
	dock_util.columns=["succ_start_station_count","succ_end_station_count","fail_start_station_count","fail_end_station_count"]
	dock_util.insert(loc=0, column='run', value=run)
	dock_util.insert(loc=1, column='station_id', value=dock_util.index)
	dock_util.reset_index(drop = True, inplace = True)
	#add run as a column to the dock_util dataframe
	# print(dock_util)

	return sim_data,moved_out_data, dock_util

PROPOSED_STATION = True

def main():

	
	n_runs = 1
	tot_customers_list= []
	kickedout_customers_list=[]
	status_list =[]
	metrics_list=[]
	station_inventory_list = []

	print("Starting simulation")
	for run in range(n_runs):
		
		customer_list=[]
		kickedout_cust =[]

		#===============================================================
		print("creating objects--- infrastructure ---")
		stations_list = []
		bike_list =[]
		if PROPOSED_STATION:
			#capacities= [15,15,20,22,18,23,17]
			no_stations =7
			station_ids = [31104,31110,31113,31114,31116,31296,40000]
			next_near= [31296,31116,31104,31116,31114,31104,31113]
			nearest_node = {x:y for x,y in list(zip(station_ids,next_near))}
			no_pedalbikes= 	[7,4,10,14,7,11,10] #63 pedal
			no_ebikes  =	[2,2,5,2,2,2,2] # 14 ebikes
			no_empty_docks= [6,9,4,6,10,10,5] 
			station_capacities= [x+y+z for x,y,z in list(zip(no_pedalbikes,no_ebikes,no_empty_docks))]
			print(station_capacities)

		else:
			#capacities= [15,14,20,22,18,23]
			no_stations =6
			station_ids = [31104,31110,31113,31114,31116,31296]
			next_near= [31296,31116,31104,31116,31114,31104]
			nearest_node = {x:y for x,y in list(zip(station_ids,next_near))}
			no_pedalbikes= 	[7,4,10,14,7,11] 
			no_ebikes  =	[2,2,5,2,2,2] 
			no_empty_docks= [6,9,4,6,10,10] 
			station_capacities= [x+y+z for x,y,z in list(zip(no_pedalbikes,no_ebikes,no_empty_docks))]
			print(station_capacities)
		

		# bike objects
	
		for j in range(0,no_stations):
			templist=[]
			for k in range(1,no_ebikes[j]+1):
				b1=bike('e'+str(k), station_ids[j],"ebike", "stationary")
				templist.append(b1)
			for m in range(1,no_pedalbikes[j]+1):
				b2=bike('p'+str(k+m), station_ids[j],"pedalbike", "stationary")
				templist.append(b2)
			bike_list.append(templist)
	

		# station objects
		for i in range(0,no_stations):
			stations_list.append(station(station_ids[i],station_capacities[i],no_empty_docks[i],no_ebikes[i],no_pedalbikes[i], bike_list[i]))
		
		#==================================================================
		print("run: {}".format(run))
		tot_customers = 0
		cust_at_time_in_out=0
		cust_at_time_out_in=0
		customer_times,customer_startinendout,customer_startoutendin = give_arrivals(PROPOSED_STATION)
		arrival_times=[]
		startin_end_out_arrival_times =[]
		startout_end_in_arrival_times=[]
		
		for i in range(len(customer_times)):
			temp_arrival_time = truncate(customer_times[i][1] * 60)
			arrival_times.append(temp_arrival_time)

		# print(arrival_times)

		for i in range(len(customer_startinendout)):
			temp_arrival_time = truncate(customer_startinendout[i][1] * 60)
			startin_end_out_arrival_times.append(temp_arrival_time)
		
		# print(startin_end_out_arrival_times)

		for i in range(len(customer_startoutendin)):
			temp_arrival_time = truncate(customer_startoutendin[i][1] * 60)
			startout_end_in_arrival_times.append(temp_arrival_time)
		# print(startout_end_in_arrival_times)
		
		#==================================================================
		#start time- simulating every minute
		
		for t in range(1,1441):
			# print("time: {}  ".format(t))

			#create in system customer objects based on poisson arrival
			cust_at_time_insys = give_customers(t,arrival_times)
			
			# for every customer spawning IN_SYSTEM system and ending ride within system start the trip
			for c in range(1,cust_at_time_insys+1):
				# print("==================================")
				# print("time: {}  ".format(t))
				cust_type = give_cust_type()
				# print("customer type is {}".format(cust_type))
				system= "in_system"
				start_station_id = give_start_station(system)
				# print("start_station_id: {}".format(start_station_id))

				#assign end station based on joint probabilities
				end_station_id = give_end_station(start_station_id,system)

				#assign bike preference based on priors
				pref_bike = give_bike_type()

				#check if preferred bike exists in station else assign alternate bike
				bike_assigned= give_bike(stations_list,start_station_id,pref_bike)
				
				if (bike_assigned != None):
					
					# print("bike assigned is {}".format(bike_assigned.bike_type))
					#duration based on fixed average durations between stations
					trip_duration= give_duration(station_ids,bike_assigned.bike_type,start_station_id,end_station_id)
					# print("trip_duration is {}".format(trip_duration))
				
					#update customer object with all the calculated fields
					if pref_bike == bike_assigned.bike_type:
						satisfaction =0
					else:
						satisfaction=2
					perm_start_station_id = start_station_id
					temp_cust= customer(len(customer_list)+1,system,cust_type,bike_assigned,t,t+trip_duration,trip_duration,perm_start_station_id,start_station_id,end_station_id,satisfaction)
					# print("cust_id is {}".format(temp_cust.cust_id))
					# print("end_time is {}".format(temp_cust.end_time))
					
					customer_list.append(temp_cust)

				else:
					trip_duration= -1 #trip duration set to -1 for bike unassigned customers
					perm_start_station_id = start_station_id
					bike_assigned = bike(9000+c, start_station_id,pref_bike, "unassigned")
					temp_cust= customer(len(kickedout_cust)+1,system,cust_type,bike_assigned,t,-1,trip_duration,perm_start_station_id,start_station_id,end_station_id,1)
					# temp_cust.giveinfo()
					kickedout_cust.append(temp_cust)
					# print("customer moved out of system due to unavailable bikes in the station")
				

			####### for customers starting outside and ending inside########
			#create in system customer objects based on poisson arrival
			cust_at_time_out_in = give_customers(t,startout_end_in_arrival_times)
		
			for p in range(1,cust_at_time_out_in+1):
				system = "out_in"
				perm_start_station_id= start_station_id =70 #outside is 70
				end_station_id= give_end_station(start_station_id,system)
				cust_type= give_cust_type()
				bike_type=give_bike_type()
				
				temp_bike_assigned = bike(1000+p, start_station_id,bike_type, "riding")
				temp_cust = customer(len(customer_list)+1,system,cust_type,temp_bike_assigned,-1,t,0,perm_start_station_id,start_station_id,end_station_id,0)
				
				customer_list.append(temp_cust)

				# print("===========================================")
				# print("time: {}  ".format(t))
				# print("cust_id is {} \n cust_sys is {} \n cust_type is {}".format(temp_cust.cust_id,temp_cust.system,temp_cust.cust_type))
				# print("end_time is {}".format(temp_cust.end_time))

			####### for customers starting inside and ending outside system########
			#create in system customer objects based on poisson arrival
			cust_at_time_in_out = give_customers(t,startin_end_out_arrival_times)
			for q in range(1,cust_at_time_in_out+1):
				system= "in_out"
				perm_start_station_id= start_station_id = give_start_station(system)
				pref_bike_type=give_bike_type()
				cust_type=give_cust_type()
				end_station_id= 70 
				temp_bike_assigned = give_bike(stations_list,start_station_id,pref_bike_type)

				
				if (temp_bike_assigned != None):
					if pref_bike_type == temp_bike_assigned.bike_type:
						satisfaction =0
					else:
						satisfaction=2

					temp_cust = customer(len(customer_list)+1,system,cust_type,temp_bike_assigned,t,-1,0,perm_start_station_id,start_station_id,end_station_id,satisfaction)
					customer_list.append(temp_cust)
				else:
					bike_assigned = bike(9500+q, start_station_id,pref_bike_type, "unassigned")
					temp_customer = customer(len(kickedout_cust)+1,system,cust_type,bike_assigned,t,-1,0,perm_start_station_id,start_station_id,end_station_id,1)
					# temp_customer.giveinfo()
					kickedout_cust.append(temp_customer)

				# print("===========================================")
				# print("time: {}  ".format(t))
				# print("cust_id is {} \n cust_sys is {} \n cust_type is {}".format(temp_cust.cust_id,temp_cust.system,temp_cust.cust_type))
				# print("start_time is {} \n end_time is {}".format(temp_cust.start_time,temp_cust.end_time))

			#-======================= Ending trip =================================
				
			# for customers who are currently in the middle of the trip, check if their trip is over.
			end_trip_customer=[]
			middleoftrip_cust=[]
			if len(customer_list) > 0:
				for cust in customer_list:
					if cust.end_time == t:
						# print("=============================")
						# print("time: {}  ".format(t))
						# print("cust id {}".format(cust.cust_id))
						# print("time is {}".format(t))
						# print("customer ending trip")
						# print("cust_id is {}".format(cust.cust_id))
						# print("start_station_id {}".format(cust.start_station_id))
						# print("end_station_id {}".format(cust.end_station_id))
						end_trip_customer.append(cust)
					elif cust.end_time>t:
						middleoftrip_cust.append(cust)
						# print("==============================")


			#end trip- check if there are empty docks, else direct to nearest station with empty dock
			if len(end_trip_customer) > 0:
				for cust in end_trip_customer:
					return_bike(station_ids,stations_list,nearest_node,t,cust)
					# print("===============================")
			
			
			

			for x in stations_list:
				station_inventory = (run,t,x.station_id,x.capacity,x.no_ebikes,x.no_pedalbikes,x.no_empty_docks)
				station_inventory_list.append(station_inventory)
				
			# print(status)
			# for cust in middleoftrip_cust:
			# 	print(cust.cust_id)

			status=(run,t,cust_at_time_insys+cust_at_time_in_out,len(end_trip_customer),len(middleoftrip_cust))
			status_list.append(status)
			tot_customers= tot_customers+cust_at_time_insys + cust_at_time_in_out +cust_at_time_out_in

		# print("=================================================================================")
		# print("=================================================================================")
		# print("simulation complete")
		print("=================================================================================")
		print("=================================================================================")
		# print_station(stations_list)
		metrics = print_metrics(run,customer_list,kickedout_cust)
		metrics_list.append(metrics)
		print("total customers= {}".format(tot_customers))
		print("tot cust who finished the ride successfully {}".format(len(customer_list)))
		print(" No of Customers who couldn't get a bike {}".format(len(kickedout_cust)))
		# print(metrics)
		
		print("=================================================================================")
		print("=================================================================================")
		sim_data,moved_out_data,dock_util = create_dataset(run, customer_list,kickedout_cust)
		
		if run == 0: #for first run, we create dockutil consolidated dataframe
			dock_util_consolidated = dock_util.copy()
			sim_data_consolidated= sim_data.copy()
			moved_out_data_consolidated = moved_out_data.copy()

		else:
			dock_util_consolidated = dock_util_consolidated.append(dock_util, ignore_index=True)
			sim_data_consolidated = sim_data_consolidated.append(sim_data, ignore_index=True)
			moved_out_data_consolidated = moved_out_data_consolidated.append(moved_out_data, ignore_index=True)
		# print(sim_data.head)
		# print(moved_out_data)
		print("=================================================================================")
		print("=================================================================================")
		
	
		#print(kickedout_cust)

		tot_customers_list.append(tot_customers)
		kickedout_customers_list.append(len(kickedout_cust))
	# print(status_list)
	station_inventory_df = pd.DataFrame.from_records(station_inventory_list, columns=["run","time","station_id","capacity","no_ebike","no_pedalbike","no_emptydock"])
	status_df = pd.DataFrame.from_records(status_list, columns =['run', 't','no_cust_start','no_cust_end','no_cust_middle']) 
	metrics_df= pd.DataFrame.from_records(metrics_list, columns =['run','succ_cust','fail_cust','diss_bike','diss_return','revenue','ecoloss','biketypeutil_ebike','biketypeutil_pedalbike','mem_util','casual_util']) 
	
	address="/Users/gkbytes/capitalbikeshare/output/"
	
	#getting output data to csv files
	dock_util_consolidated.to_csv(address+"dock_util_consolidated_prop.csv", index=False)
	station_inventory_df.to_csv(address+"station_inventory_prop.csv",index=False)
	metrics_df.to_csv(address+"metrics_df_prop.csv",index=False)
	status_df.to_csv(address+"status_df_prop.csv",index=False)
	sim_data_consolidated.to_csv(address+"sim_data_consolidated_prop.csv",index=False)
	moved_out_data_consolidated.to_csv(address+"moved_out_data_consolidated_prop.csv",index=False)


	# print(station_inventory.head)
	# print(moved_out_data_consolidated)
	# print(dock_util_consolidated.shape)
	# print(dock_util_consolidated)
	# print(sim_data)
	# print(status_df.tail(50))
	# print(metrics_df.head)

if __name__ == "__main__":
	main()


