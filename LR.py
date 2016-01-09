''' The plan is to rewrite and this time, calculate cost each time to ensure its reducing. Also make it  enough to handle multiple variables '''
from __future__ import division
import os
import sys

def computecost(X,Y,theta):
	#X is the feature vector, Y is the predicted variable
	h_theta = calculatehTheta(X,theta)
	delta = (h_theta - Y) * (h_theta - Y)
	return (1/194) * delta 



def allCost(f, no_features):
	theta = [0,0]
	sigma = 0
	data = open(f,'r')
	for line in data:
		X=[]
		Y=0
		points=line.split(",")
		for i in range(no_features):
			X.append(float(points[i]))
		Y = float(points[no_features].strip("\n"))
		sigma = sigma + computecost(X, Y, theta)
	return sigma

def calculatehTheta(points, theta):
	#This takes a file which has  (1,feature1,feature2,so ... on)
	#print 'Points are',points
	sigma  = 0 
	for i in range(len(theta)):
		sigma = sigma + theta[i] * float(points[i])
	return sigma



def gradient_Descent(f, no_iters, no_features, theta):
	''' Calculate ( h(x) - y ) * xj(i). And then subtract it from thetaj. Continue for 1500 iterations and you will have your answer'''
	
	
	X = []
	Y = 0
	sigma = 0
	alpha = 0.01
	for i in range(no_iters):
		for j in range(len(theta)):
			data = open(f, 'r')
			for line in data:
				points = line.split(",")
				for i in range(no_features):
					X.append(float(points[i]))
				Y = float(points[no_features].strip("\n"))
				h_theta = calculatehTheta(points,theta)
				delta = h_theta - Y
				sigma = sigma + delta * float(points[j])
			data.close()
			theta[j] = theta[j] - (alpha/97) * sigma

			sigma = 0
	print theta

print allCost(sys.argv[1],2)
print gradient_Descent(sys.argv[1],1500,2,[0,0])
