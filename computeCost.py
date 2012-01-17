from __future__ import division
def computeCost(f):
	#Pass it the data file with x and y ,  and return back J(theta)
	data = open(f,'r')
	sigma = 0
	for line in data:
		points = line.split(",") #This gives you x and y 
		h_theta = theta_0 * 1 + theta_1 * float(points[0])
		delta = (h_theta - float(points[1].strip("\n"))) * (h_theta - float(points[1].strip("\n")))
		sigma = sigma + delta 
	return (1/194) * sigma
print computerCost(sys.argv[1])
