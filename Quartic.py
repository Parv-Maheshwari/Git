import numpy as np
import matplotlib.pyplot as plt
import math 
import config

class Quartic_path:
    def __init__(self, s_start, sv_start,sa_start, sv_end, sa_end,T):
        self.s_start = s_start
        self.sv_start = sv_start
        self.sa_start = sa_start
        self.sv_end = sv_end
        self.sa_end = sa_end
        
        self.a0 = sa_start
        self.a1 = sv_start
        self.a2 = sa_start / 2.0

        A = np.array([[3 * T ** 2, 4 * T ** 3],
                      [6 * T, 12 * T ** 2]])
        
        b = np.array([sv_end - self.a1 - 2 * self.a2 * T,
                      sa_end - 2 * self.a2])
        x = np.linalg.solve(A, b)

        self.a3 = x[0]
        self.a4 = x[1]
        
        self.p = np.poly1d([self.a4, self.a3, self.a2, self.a1, self.a0])
        self.p_d = np.poly1d([4*self.a4, 3*self.a3, 2*self.a2, self.a1])
        self.p_dd = np.poly1d([12*self.a4, 6*self.a3, 2*self.a2, self.a1])
        self.p_ddd = np.poly1d([24*self.a4, 6*self.a3, 2*self.a2])

        
    def show_quartic(self):
        T = np.linspace(2,10,100)
        y = self.a4*T**4+self.a3*T**3+self.a2*T**2+self.a1*T+self.a0
        plt.plot(T,y, 'r')
        plt.show
        
    
    def quartic_t_at_s(self, s):
        p = np.poly1d([self.a4, self.a3, self.a2, self.a1, self.a0 - s])
        t = p.r[0] 
        return t
    
    def quartic_at(self, t):
        p = np.poly1d([self.a4, self.a3, self.a2, self.a1, self.a0])
        s = p(t)
        return s
    