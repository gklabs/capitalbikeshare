
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
	def __init__(self,station_id,bikeid,bike_type,status):
		self.bikeid= bikeid
		self.station= station_id
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

	def UpdateNumberofBikes(self,option):

		print("updating the bikes in the stations")

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
    templist=[]
    for j in range(0,6):
    	for k in range(1,no_ebikes[j]):
    		b1=bike(k, j,"ebike", "stationary")
    		templist.append(b1)
    	for m in range(1,no_pedalbikes[j]):
    		b2=bike(k+m, j,"pedalbike", "stationary")
    		templist.append(b2)
    	bike_list.append(templist)


    #station objects
    for i in range(0,6):
    	stations_list.append(station(station_ids[i],station_capacities[i],no_empty_docks[i],no_ebikes[i],no_pedalbikes[i], bike_list[i]))

    #==================================================================
    #start time- simulating every minute
    for t in range(1,1441):
    	print("time: {}  ".format(t))

    #create customer objects based on poisson arrival
    cust_at_time = 5 # set poisson
    for c in range(0,cust_at_time):
    	
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
    	end_station_joint_dist = [[0.089552,0.253731,0.089552,0.199005,0.233831,0.134328],[0.142857,0.133641,0.82949,0.267281,0.119816,0.253456],[0.066986,0.320574,0.100478,0.157895,0.143541,0.210526],[0.205357,0.379464,0.049107,0.102679,0.044643,0.218750],[0.231884,0.239130,0.108696,0.101449,0.086957,0.231884],[0.117885,0.264228,0.191057,0.186992,0.138211,0.101525]]

    	#assign bike preference based on priors
    	pedal_ebike= random.uniform(0,1)
    	if pedal_ebike>= 0.881335:
    		pedal_ebike= "pedal"
    	else:
    		pedal_ebike ="ebike"

    	#check if preferred bike exists in station else assign alternate bike

    	#start trip- create delay for customers starting trip

    	#end trip- check if there are empty docks, else direct to nearest station with empty dock




if __name__ == "__main__":
    main()


