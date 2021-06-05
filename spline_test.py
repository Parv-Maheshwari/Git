
import numpy as np
import matplotlib.pyplot as plt
import math 
import config
import Splines

x = [1,2,3,4,5]
y = [3,5,8,3,5]

cs = Splines.Spline_trajectory(x,y)
cs.show_splines()
plt.show()