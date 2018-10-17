# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def GetDataMeanSigma2(N):
    data = np.random.randn(N)
    mean = sum(data)/N
    sigma2 = sum(pow((data-mean),2))/N
    return (mean, sigma2)

def MonteCarloSimulation (fig, N):

    N_monte_carlo = 10000
    points = [N] * N_monte_carlo

    stats = map(GetDataMeanSigma2, points)

    mean, sigma2 = zip(*stats)

    d = mean/(np.sqrt(sigma2)/np.sqrt(N))

    plt.figure(fig)
    n, bins, patches = plt.hist(d, 600, normed = 1, facecolor = 'blue', alpha = 1)

    y = mlab.normpdf(bins, 0, 1)

    l = plt.plot(bins, y, 'r', linewidth = 2)

    plt.title('PDF of '+r'$\bar{x}$'+'/'+'('+u'\u03c3'+'/'+r'$\sqrt{N}$'+')'+'for N = 100')
    plt.axis([-6.5, 6.5, 0, 0.5])
    plt.grid(True)

    plt.show()

MonteCarloSimulation(1, 10)
MonteCarloSimulation(2, 100)
