import numpy as np
import matplotlib.pyplot as plt
import math 

class Quintic_path:
    def __init__(self, d_start, dv_start,da_start, d_end, dv_end, da_end,T):
        self.d_start = d_start
        self.dv_start = dv_start
        self.da_start = da_start
        self.d_end = d_end
        self.dv_end = dv_end
        self.da_end = da_end
        
        self.a0 = d_start
        self.a1 = dv_start
        self.a2 = da_start / 2.0

        A = np.array([[T**3, T**4, T**5],
                      [3 * T ** 2, 4 * T ** 3, 5 * T ** 4],
                      [6 * T, 12 * T ** 2, 20 * T ** 3]])
        b = np.array([d_end - self.a0 - self.a1 * T - self.a2 * T**2,
                      dv_end - self.a1 - 2 * self.a2 * T,
                      da_end - 2 * self.a2])
        x = np.linalg.solve(A, b)

        self.a3 = x[0]
        self.a4 = x[1]
        self.a5 = x[2]
        self.p = np.poly1d([self.a5 ,self.a4, self.a3, self.a2, self.a1, self.a0])
        self.p_d = np.poly1d([5*self.a5 ,4*self.a4, 3*self.a3, 2*self.a2, self.a1])
        self.p_dd = np.poly1d([20*self.a5 ,12*self.a4, 6*self.a3, 2*self.a2, self.a1])
        self.p_ddd = np.poly1d([60*self.a5 ,24*self.a4, 6*self.a3, 2*self.a2])
        
        
    def show_quintic(self,T):
        T = np.linspace(0,T,100)
        y = self.a5*T**5+self.a4*T**4+self.a3*T**3+self.a2*T**2+self.a1*T+self.a0
        plt.plot(T,y, 'r')
        plt.grid(True)
        plt.show()
              
    def quintic_at(self, t):
        p = np.poly1d([self.a5 ,self.a4, self.a3, self.a2, self.a1, self.a0])
        d = p(t)
        return d
        
