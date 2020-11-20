
import random
import numpy as np
import scipy


class customer:
	def __init__(self,cust_id,cust_type,bike,start_time, end_time,duration,start_station_id,end_station_id ):
		self.cust_id= cust_id
		self.cust_type= cust_type
		self.bike = bike #assigns the bike object to the customer
		self.start_time= start_time
		self.end_time= end_time
		self.duration=duration
		self.start_station_id= start_station_id
		self.end_station_id= end_station_id
		

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

	def UpdateNumberofBikes(self,biketype_assigned):

		print("updating the bikes in the station")
		if biketype_assigned=="pedalbike":
			self.no_pedalbikes-=self.no_pedalbikes
		else:
			self.no_ebikes-=self.no_ebikes

		self.no_empty_docks+=self.no_empty_docks

		#removing bike from the station's bikelist is done in give_bike function


def give_end_station(start_station_id):
	station_ids = [31104,31110,31113,31114,31116,31296]
	end_index= station_ids.index(start_station_id)

	end_station_joint_dist = np.array([[0.089552,0.253731,0.089552,0.199005,0.233831,0.134328],[0.142857,0.133641,0.82949,0.267281,0.119816,0.253456],[0.066986,0.320574,0.100478,0.157895,0.143541,0.210526],[0.205357,0.379464,0.049107,0.102679,0.044643,0.218750],[0.231884,0.239130,0.108696,0.101449,0.086957,0.231884],[0.117885,0.264228,0.191057,0.186992,0.138211,0.101525]])

	cust_end_node_cdf= end_station_joint_dist[index]

	cust_end_node = random.uniform(0,1)
	if cust_end_node <=cust_end_node_cdf[0]:
    		end_station_id= 31104
    	elif cust_end_node > cust_end_node_cdf[0] and cust_end_node <= cust_end_node_cdf[1] :
    		end_station_id= 31110
    	elif cust_end_node > cust_end_node_cdf[1] and cust_end_node <= cust_end_node_cdf[2] :
    		end_station_id= 31113
    	elif cust_end_node > cust_end_node_cdf[2] and cust_end_node <= cust_end_node_cdf[3] :
    		end_station_id= 31114
    	elif cust_end_node > cust_end_node_cdf[3] and cust_end_node <= cust_end_node_cdf[4] :
    		end_station_id= 31116
    	elif cust_end_node > cust_end_node_cdf[4] and cust_end_node <= cust_end_node_cdf[5] :
    		end_station_id= 31296
	
	return end_station_id

# This function gives the duration based on the start and end stations
def give_duration(bike_type,start_station_id,end_station_id):
	station_ids = [31104,31110,31113,31114,31116,31296]
	start_index= station_ids.index(start_station_id)
	end_index = station_ids.index(end_station_id)

	#matrix for duration
	ebike_duration_matrix= np.array([[10,10,10,10,10,10],
		[10,10,10,10,10,10],
		[10,10,10,10,10,10],
		[10,10,10,10,10,10],
		[10,10,10,10,10,10],
		[10,10,10,10,10,10]])

	pedal_duration_matrix= np.array([[10,10,10,10,10,10],
		[10,10,10,10,10,10],
		[10,10,10,10,10,10],
		[10,10,10,10,10,10],
		[10,10,10,10,10,10],
		[10,10,10,10,10,10]])

	return duration_matrix[start_index][end_index]

def give_bike(stations_list,start_station_id,pref_bike):

	print("assigning bike")

	# check if preferred bike exists in start station
	for x in stations_list:
		if start_station_id == x.station_id:
			station_index= stations_list.index(x)
	
	if pref_bike == "ebike":
		if stations_list[station_index].no_ebikes !=0:
			flag=1
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="ebike":
					stations_list[station_index].bike_list.remove(y)
					y.status="riding"
					return y
			
		else:
			flag=0
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="pedalbike":
					stations_list[station_index].bike_list.remove(y)
					y.status="riding"
					return y
	else: # preferred bike is pedal bike
		if stations_list[station_index].no_pedalbikes !=0:
			flag=1
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="pedalbike":
					stations_list[station_index].bike_list.remove(y)
					y.status="riding"
					return y
		else:
			flag=0
			for y in stations_list[station_index].bike_list:
				if y.bike_type=="ebike":
					stations_list[station_index].bike_list.remove(y)
					y.status="riding"
					return y


def main():
    print("Hello World!")

    #create pre-existing objects
    station_ids = [31104,31110,31113,31114,31116,31296]
    stations_list = []
    bike_list =[]
    tot_bikes= 72
    #dummy numbers
    station_capacities= [10,15,15,10,12,10]
    no_empty_docks= [1,2,1,2,1,2]
    no_pedalbikes= [5,8,9,5,6,4]
    no_ebikes  =[4,5,5,4,6,4]

    # durations are a 6x6 matrix (how?)
    pedal_trip_duration= 15
    ebike_trip_duration= 10

    # bike objects
    for j in range(0,6):
    	templist=[]
    	for k in range(1,no_ebikes[j]):
    		b1=bike('e'+k, station_ids[j],"ebike", "stationary")
    		templist.append(b1)
    	for m in range(1,no_pedalbikes[j]):
    		b2=bike('p'+k+m, station_ids[j],"pedalbike", "stationary")
    		templist.append(b2)
    	bike_list.append(templist)


    #station objects
    for i in range(0,6):
    	stations_list.append(station(station_ids[i],station_capacities[i],no_empty_docks[i],no_ebikes[i],no_pedalbikes[i], bike_list[i]))

    #==================================================================
    tot_customers = 0
    customer_list=[]
    #start time- simulating every minute
    for t in range(1,1441):
    	print("time: {}  ".format(t))

    	#create customer objects based on poisson arrival
	    cust_at_time = 5 # set poisson

	    # for every customer spawning new in the system start the trip
	    for c in range(1,cust_at_time+1):

	    	# casual vs member (0.2810 vs 0.7189)
	    	casual_member= random.uniform(0,1)
	    	if casual_member>= 0.718929:
	    		cust_type= "casual"
	    	else:
	    		cust_type ="member"

	    	#assign customer to  start station and end station based on priors
	    	cust_start_node = random.uniform(0,1)
	    	cust_start_node_cdf = [0.162753,0.338462,0.507693,0.689070,0.800811,1]

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

	    	#duration based on fixed average durations between stations
	    	trip_duration= give_duration(biketype_assigned.bike_type,start_station_id,end_station_id)

	    	#update customer object with all the calculated fields
	    	customer_list.append(customer(tot_customers+c,cust_type,bike_assigned,t,t+duration,duration,start_station_id,end_station_id))

	    	#update bike in start station
	    	#call update bike function for the station object
	    	for x in stations_list:
				if start_station_id == x.station_id:
					x.UpdateNumberofBikes(bike_assigned.bike_type)


		# for customers who are currently in the middle of the trip, check if their trip is over.
		end_trip_customer=[]
		for cust in customer_list:
			if cust.end_time == t:
				print("customer ending trip")
				end_trip_customer.append(cust)


	    #end trip- check if there are empty docks, else direct to nearest station with empty dock
	    for cust in end_trip_customer:
	    	for s in stations_list:
	    		if s.station_id==cust.end_station_id:
	    			if s.no_empty_docks !=0:
	    				print("empty dock available to return")
	    				s.bike_list.append(cust.bike)
	    				s.no_empty_docks-=1
	    				cust.bike.current_station=s.station_id
	    				cust.bike.status= "stationary"
	    				end_trip_customer.remove(cust)
	    			else:
	    				print("no empty dock available, redirecting to another station")
	    				for ids in station_ids:
	    					if cust.end_station_id==ids:
	    						cust.end_station_id = station_ids[station_ids.index(ids)+1]





	    #update bike in end station
	    tot_customers= tot_customers+cust_at_time


if __name__ == "__main__":
    main()


