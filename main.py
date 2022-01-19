#%% Imports
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import random 
from matplotlib import style
style.use('dark_background')

#%%Class definitions

class Oslo():

    def __init__(self, length, threshold):
        self.length = length 
        self.threshold = threshold
        self.heights = np.zeros(self.length)
        self.thresholds = np.zeros(self.length)
        self.thresholds = [random.choice([1,2]) for i in self.thresholds]
        self.count_n_grains = 0
        self.count_n_relax = 0

    def all_heights(self):
        """ Returns an array of the height of each point """
        height = self.heights
        return height

    def all_thresholds(self):
        """ Returns an array of the threshold slope of each point """
        thresholds = self.thresholds
        return thresholds

    def add_grain(self, ind1):
        """Process to add a grain to a point at index i (i-1 really since starts at 0)"""
        if ind1 < self.length:
            #np.put(self.heights, ind1, self.heights[ind1] +1)
            self.heights[ind1] = self.heights[ind1] + 1

    def lose_grain(self, ind2):
        """Process of loosing a grain from a point at index i (i-1 in reality)"""
        #np.put(self.heights, ind2, self.heights[ind2] -1)
        self.heights[ind2] = self.heights[ind2] -1

    def relax(self, ind3):
        """Process of the relaxation of a point"""
        self.add_grain(ind1 = ind3+1)
        self.lose_grain(ind2 = ind3)
        self.thresholds[ind3] = random.choice([1,2])
    
    def slopes(self):
        """Returns an array of the slopes of all points"""
        current_slope = np.zeros(self.length)
        current_slope = [self.heights[i] - self.heights[i+1] for i in range(len(self.heights)-1)]# self.heights[-1])
        current_slope = np.append(current_slope,self.heights[-1])
        return current_slope

    def indicies_to_change(self):
        """Returns an array of indicies that unstable"""
        self.current_slopes = self.slopes()
        indexs = []
        for i in range(0, len(self.current_slopes)):
            if self.current_slopes[i]> self.thresholds[i]:
                indexs.append(i)
        return indexs

    def drop_grain(self):
        """Simulates droping a grain at the i=0 (the first point)"""
        self.add_grain(ind1 = 0)
        unstable = self.indicies_to_change()
        self.count_n_grains +=1
        while len(unstable) != 0:
            for i in unstable:
                self.relax(ind3 = i)
                self.count_n_relax +=1
                #plt.plot(np.linspace(0,5,5),model.all_heights())
                unstable = self.indicies_to_change()

    def height(self):
        """Returns the height of the pile at i=0"""
        height = self.heights[0]
        return height

        
#%%
L = [4,8,16,32,64,128,256, 512]
for i in L:
    model = Oslo(length = i, threshold = [1,2])
    for j in range(1000):
        model.drop_grain()
        


#%% 
"""Set test as given by document"""
model = Oslo(length = 16, threshold = [1,2])
height = np.array([])
for i in range(10000):
    model.drop_grain()
    height = np.append(height, model.height())


plt.plot(range(len(height)), height)
plt.show()
average = np.average(height[500:])
print(average)

model = Oslo(length = 32, threshold = [1,2])
height = np.array([])
for i in range(10000):
    model.drop_grain()
    height = np.append(height, model.height())


plt.plot(range(len(height)), height)
plt.show()
average = np.average(height[1000:])
print(average)


#%%