import Quintic

D_START = 1
DV_START = 2
DA_START = 3
D_END = 5
DV_END = 3
DA_END = 1
T = 5

quin = Quintic.Quintic_path(D_START, DV_START,DA_START, D_END, DV_END, DA_END,T)

quin.show_quintic(T)
