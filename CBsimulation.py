
import random
import numpy as np
import scipy
import bisect
import pandas as pd
import matplotlib.pyplot as plt

#PROPOSED_STATION = True
PROPOSED_STATION = False

class customer:
	def __init__(self,cust_id,cust_type,bike,start_time, end_time,duration,start_station_id,start_station_id,end_station_id,satisfaction ):
		self.cust_id= cust_id
		self.cust_type= cust_type
		self.bike = bike #assigns the bike object to the customer
		self.start_time= start_time
		self.end_time= end_time
		self.duration=duration
		self.perm_start_station_id = start_station_id
		self.start_station_id= start_station_id
		self.end_station_id= end_station_id
		self.satisfaction = satisfaction #0 means satisfied, 1 means dissatisfied
		

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

		print("updating the bikes in the station")

		if kind == "pickup":
			self.no_empty_docks+=1
			if biketype_assigned=="pedalbike":
				self.no_pedalbikes-=1
			else:
				self.no_ebikes-=1

			
		#removing bike from the station's bikelist is done in give_bike function
		else: #return a bike
			self.no_empty_docks-=1
			if biketype_assigned=="pedalbike":
				self.no_pedalbikes+=1

			else:
				self.no_ebikes+=1


def give_end_station(start_station_id):

	if PROPOSED_STATION:
		station_ids = [31104,31110,31113,31114,31116,31296,10000]
	else:
		station_ids = [31104,31110,31113,31114,31116,31296]
	end_index= station_ids.index(start_station_id)
	end_station_id =0

	if PROPOSED_STATION:
		pass
	else:
		end_station_joint_dist = np.array([[0.089562,0.253732,0.089552,0.199005,0.233831,0.134328],[0.142857,0.133641,0.082949,0.267281,0.119816,0.253456],[0.066986,0.320574,0.100478,0.157895,0.143541,0.210526],[0.205357,0.379464,0.049107,0.102679,0.044643,0.218750],[0.231884,0.239130,0.108696,0.101449,0.086957,0.231884],[0.117887,0.26442,0.191057,0.186992,0.138211,0.101525]])

	cust_end_node_cdf_temp= end_station_joint_dist[end_index]
	cust_end_node_cdf =[]
	y=0
	x=0
	for x in cust_end_node_cdf_temp:
		y=y+x
		cust_end_node_cdf.append(y)

	cust_end_node = random.uniform(0,1)
	# print("end station proba {}".format(cust_end_node))

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
	print("end station_id is {}".format(end_station_id))
	return end_station_id

# This function gives the duration based on bike type, the start and end stations
def give_duration(bike_type,start_station_id,end_station_id):
	
	start_index= station_ids.index(start_station_id)
	end_index = station_ids.index(end_station_id)

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
		if stations_list[station_index].no_ebikes >0:
			flag=1
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="ebike":
					stations_list[station_index].bike_list.remove(y)
					# stations_list[station_index].UpdateNumberofBikes(y.bike_type,"pickup")
					stations_list[station_index].no_ebikes-=1
					stations_list[station_index].no_empty_docks+= 1
					y.status="riding"
					return y
			
		else:
			flag=0
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="pedalbike":
					stations_list[station_index].bike_list.remove(y)
					# stations_list[station_index].UpdateNumberofBikes(y.bike_type,"pickup")
					stations_list[station_index].no_pedalbikes-=1
					stations_list[station_index].no_empty_docks+= 1
					
					y.status="riding"
					return y
	else: # preferred bike is pedal bike
		if stations_list[station_index].no_pedalbikes >0:
			flag=1
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="pedalbike":
					stations_list[station_index].bike_list.remove(y)
					# stations_list[station_index].UpdateNumberofBikes(y.bike_type,"pickup")
					stations_list[station_index].no_pedalbikes-=1
					stations_list[station_index].no_empty_docks+= 1
					y.status="riding"
					return y
		else:
			flag=0
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="ebike":
					stations_list[station_index].bike_list.remove(y)
					# stations_list[station_index].UpdateNumberofBikes(y.bike_type,"pickup")
					stations_list[station_index].no_ebikes-=stations_list[station_index].no_ebikes
					stations_list[station_index].no_empty_docks+= stations_list[station_index].no_empty_docks
					y.status="riding"
					return y

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier
#===============================================================
'''
implementing thinning algorithm

'''
def give_arrivals():

	SEED = None
	MAXSEEDSEQ = 100000
	u1count = 0
	counter = 0

	# *** OUTPUT: customer_times[] contains customer arrival times tuple (customer #, arrival time (hr))

	## code below

	random.seed(SEED)
	U1 = [random.uniform(0,1) for i in range(MAXSEEDSEQ)] # contains sequence of random #s U(0,1)
	poisson1rate = [0] # stores uniform poisson arrival rates lambda == 1


	#define inverse transform functions here

	def eq1(x): return (x/0.258)
	def eq2(x): return (x+3.95)/1.048
	def eq3(x): return ((x+2.2)/.874)
	def eq4(x): return ((x+15)/1.626)
	def eq5(x): return ((x+7.76)/1.282)
	def eq6(x): return ((x+30.72)/2.28)

	vhrthin = pd.read_csv("thinningdata.csv")


	for i in range(24):
	    test = poisson1rate[i] - np.log(U1[counter])
	    while (test >= 21.72 and eq6(test) >= 24) or test >= 24: # trim domain/range [0,24) of poisson generated value
	        counter += 1
	        test = poisson1rate[i] - np.log(U1[counter])

	    poisson1rate.append(test)
	    counter += 1

	poisson1rate.pop(0) # in place


	#cdf inv equations

	'''
	eq1: y=.214x + 0.22 inv_range: (0,1.29) [0-5] eq1

	eq2: y=1.048x - 3.95 range: 1.29-6.53 [5-10] eq2

	eq3: y=0.874x - 2.2 range: 6.53-12.65 [10-17] eq3 

	eq4: y=1.626x - 15 range: 12.65-19.156 [17-21] eq4

	eq5: y= 1.282x - 7.76 range: 19.156 - 21.72 [21-23] eq5

	eq6: y=2.28x - 30.72, range: 21.72-24 [23-24] eq6
	'''


	flist = [0,eq1,eq2,eq3,eq4,eq5,eq6]

	# define right sets inverse domain = f(x) range
	places = [
	    (1.29, '1'),
	    (6.53, '2'),
	    (12.65, '3'),
	    (19.156, '4'),
	    (21.72, '5'),
	    (24, '6')
	]

	places.sort() # list must be sorted
	pos_log = []

	for to_find in poisson1rate:
	    pos = bisect.bisect_right(places, (to_find,))
	    pos_log.append(pos)
	  #  print ('%s -> %s' % (to_find, places[pos]))

	times_list = [(poisson1rate[x],places[pos_log[x]]) for x in range(len(pos_log))]

	customer = 1
	customer_times = []

	for x in range(len(times_list)):
	    arrtime = flist[int(times_list[x][1][1])](times_list[x][0])
	    customer_times.append((customer, arrtime))
	    customer += 1

	# print(customer_times)
	return customer_times

def give_customers(t,arrival_times):

	no_cust_at_time= 0
	for time in arrival_times:
		if time == t:
			no_cust_at_time+=1

	return no_cust_at_time




#===============================================================

def return_bike(t,cust):
	for s in stations_list:
				if s.station_id==cust.end_station_id:
					if s.no_empty_docks !=0:
						print("empty dock available to return")
						s.bike_list.append(cust.bike)
						cust.bike.current_station=s.station_id
						cust.bike.status= "stationary"
						s.UpdateNumberofBikes(cust.bike.bike_type, "return")
						# end_trip_customer.remove(cust)

					else:
						print("no empty dock available, redirecting to another station")
						for ids in station_ids:
							if cust.end_station_id==ids:
								#start station must be the initial end station
								cust.start_station_id=cust.end_station_id
								#assign the next station from the list as end station
								cust.end_station_id = nearest_node[cust.end_station_id]
								#change duration
								cust.duration= give_duration(cust.bike.bike_type,cust.start_station_id,cust.end_station_id)
								cust.end_time= t + cust.duration
								cust.satisfaction=1




#===============================================================
print("creating objects--- infrastructure ---")
if PROPOSED_STATION:
	station_ids = [31104,31110,31113,31114,31116,31296,10000]

else:
	station_ids = [31104,31110,31113,31114,31116,31296]
	next_near= [31296,31116,31104,31116,31114,31104]

nearest_node = {x:y for x,y in list(zip(station_ids,next_near)}
stations_list = []
bike_list =[]

if PROPOSED_STATION:
	tot_bikes = 82
else:
	tot_bikes= 72
#dummy numbers
if PROPOSED_STATION:
	no_pedalbikes= 	[11,1,10,3,16,12,9]
	no_ebikes  =	[2,2,2,2,2,2,1]
	no_empty_docks= [14,13,19,19,12,10,5]
	station_capacities= [x+y+z for x,y,z in list(zip(no_pedalbikes,no_ebikes,no_empty_docks))]
	print(station_capacities)
else:
	no_pedalbikes= 	[11,1,10,3,16,12]
	no_ebikes  =	[2,2,2,2,2,2]
	no_empty_docks= [14,13,1,19,12,1]
	station_capacities= [x+y+z for x,y,z in list(zip(no_pedalbikes,no_ebikes,no_empty_docks))]
	print(station_capacities)

# bike objects
if PROPOSED_STATION:
	for j in range(0,7):
		templist=[]
		for k in range(1,no_ebikes[j]):
			b1=bike('e'+str(k), station_ids[j],"ebike", "stationary")
			templist.append(b1)
		for m in range(1,no_pedalbikes[j]):
			b2=bike('p'+str(k+m), station_ids[j],"pedalbike", "stationary")
			templist.append(b2)
		bike_list.append(templist)
else:
	for j in range(0,6):
		templist=[]
		for k in range(1,no_ebikes[j]+1):
			b1=bike('e'+str(k), station_ids[j],"ebike", "stationary")
			templist.append(b1)
		for m in range(1,no_pedalbikes[j]+1):
			b2=bike('p'+str(k+m), station_ids[j],"pedalbike", "stationary")
			templist.append(b2)
		bike_list.append(templist)

#station objects
if PROPOSED_STATION:
	for i in range(0,7):
		stations_list.append(station(station_ids[i],station_capacities[i],no_empty_docks[i],no_ebikes[i],no_pedalbikes[i], bike_list[i]))
else:
	for i in range(0,6):
		stations_list.append(station(station_ids[i],station_capacities[i],no_empty_docks[i],no_ebikes[i],no_pedalbikes[i], bike_list[i]))
#==================================================================

##### reading duration from the csv file
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



def main():
	print("Starting simulation")
	customer_times = give_arrivals()
	arrival_times=[]
	for i in range(len(customer_times)):
		temp_arrival_time = truncate(customer_times[i][1] * 60)
		arrival_times.append(temp_arrival_time)

	#create pre-existing objects
	#==================================================================
	tot_customers = 0
	customer_list=[]
	
	#start time- simulating every minute
	for t in range(1,1441):
		# print("time: {}  ".format(t))

		#create customer objects based on poisson arrival
		cust_at_time = give_customers(t,arrival_times)
		# for every customer spawning new in the system start the trip
		for c in range(1,cust_at_time+1):
			print("==================================")
			print("time: {}  ".format(t))
			# casual vs member (0.2810 vs 0.7189)
			casual_member= random.uniform(0,1)
			if casual_member>= 0.718929:
				cust_type= "casual"
			else:
				cust_type ="member"
			print("customer type is {}".format(cust_type))

			#assign customer to  start station and end station based on priors
			cust_start_node = random.uniform(0,1)
			if PROPOSED_STATION:
				pass #TODO
			else:
				cust_start_node_cdf = [0.162753,0.338462,0.507693,0.689070,0.800811,1]
			if PROPOSED_STATION:
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
					start_station_id= 10000
			else:
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
			print("start_station_id: {}".format(start_station_id))

			#assign end station based on joint probabilities
			end_station_id = give_end_station(start_station_id)

			#assign bike preference based on priors
			pedal_ebike= random.uniform(0,1)
			if pedal_ebike>= 0.881335:
				pref_bike= "pedal"
			else:
				pref_bike ="ebike"

			#check if preferred bike exists in station else assign alternate bike
			bike_assigned= give_bike(stations_list,start_station_id,pref_bike)
			print("bike assigned is {}".format(bike_assigned.bike_type))
			#duration based on fixed average durations between stations
			trip_duration= give_duration(bike_assigned.bike_type,start_station_id,end_station_id)
			print("trip_duration is {}".format(trip_duration))
			

			#update customer object with all the calculated fields
			temp_cust= customer(tot_customers+c,cust_type,bike_assigned,t,t,t+trip_duration,trip_duration,start_station_id,end_station_id,0)
			customer_list.append(temp_cust)
			print("cust_id is {}".format(temp_cust.cust_id))
			print("end_time is {}".format(temp_cust.end_time))

			#update bike in start station
			#call update bike function for the station object
			# for x in stations_list:
			# 	if start_station_id == x.station_id:
			# 		x.UpdateNumberofBikes(bike_assigned.bike_type,"pickup")
			# 		break

		# for customers who are currently in the middle of the trip, check if their trip is over.
		end_trip_customer=[]
		
		if len(customer_list) > 0:
			for cust in customer_list:
				if cust.end_time == t:
					print("=============================")
					# print("time: {}  ".format(t))
					# print("cust id {}".format(cust.cust_id))
					print("time is {}".format(t))
					print("customer ending trip")
					print("cust_id is {}".format(cust.cust_id))
					print("start_station_id {}".format(cust.start_station_id))
					print("end_station_id {}".format(cust.end_station_id))
					end_trip_customer.append(cust)
					print("==============================")


		#end trip- check if there are empty docks, else direct to nearest station with empty dock
		if len(end_trip_customer) > 0:
			for cust in end_trip_customer:
				return_bike(t,cust)
				print("===============================")


		#update bike in end station
		tot_customers= tot_customers+cust_at_time
	print("total customers= {}".format(tot_customers))


if __name__ == "__main__":
	main()


