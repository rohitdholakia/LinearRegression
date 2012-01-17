def gradient_descent(no_iters):
	''' Plan :   1 . You iterate a fixed number of times . you fixed that at no_iters
				 2 . In each iteration , you calculate  the sigma of the h_theta * sample training 
				 3 . Update theta
	'''
	theta_0 = 0
	theta_1 = 0
	thetas = [theta_0,theta_1]
	alpha = 0.01
	
	FACTOR = alpha/97
	for i in range(no_iters): #For 1500 iterations
		#print 'In iteration',i,' thetas are ',thetas
		for j in range(0,2): #For each theta
			data = open(sys.argv[1],'r')		
			sigma = 0

			for line in data: #Calculate cost
				points = line.split(",")
				delta = (thetas[0] * 1 + thetas[1] * float(points[0]) ) - float(points[1]) #Calculating h(theta)
				if(j==0):
					sigma = sigma + delta * 1
				else:
					sigma = sigma + delta * float(points[0])
			
			thetas[j] = thetas[j] - (FACTOR*sigma) #Find out the new theta and substitute it 
			data.close()
			

	print thetas
	print 'Final regression equation is',thetas[0],"+",thetas[1],"*x"
import os,sys
gradient_descent(1500)
