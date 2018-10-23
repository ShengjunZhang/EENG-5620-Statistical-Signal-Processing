# -*- coding: utf-8 -*-
#---------------------------------------------------------------#
# Copyright 2018, Shengjun(Zhang) Zhang, All rights reserved.
#---------------------------------------------------------------#
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import sys

def GenerateData(N):
	mu = 1
	N = 50
	sigma_square = 0.1
	sigma = np.sqrt(sigma_square/N)
	data = sigma * np.random.randn(N) + mu
	return(data)

def MonteCarloSimulation (fig, N):

	N_monte_carlo = 5000
	points = [N] * N_monte_carlo

	stats = map(GenerateData, points)

	data = zip(*stats)

	plt.figure(fig)
	n, bins, patches = plt.hist(data, 50, normed =1, facecolor = 'blue', alpha = 1)

	# The normal distribution with mu = 1, sigma = square root of 0.1/N
	mu = 1
	sigma_square = 0.1
	sigma = np.sqrt(sigma_square/N)
	y = mlab.normpdf(bins, mu, sigma)
	l = plt.plot(bins, y, 'r', linewidth = 2)

	plt.title('M = 5000')
	plt.axis([0, 2, 0, 20])
	plt.grid(True)

	plt.show()

MonteCarloSimulation(1, 50)
