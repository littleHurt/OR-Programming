# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 2020

@author: littleHurt
"""


# https://docs.google.com/document/d/1mhKLc4LEIVvP0jUudIO2_WpOFF7knHA6Agmgbi6if3E/edit

import pandas as pd
import numpy as np
from mip import *

# set initail model
m = Model(sense = MINIMIZE, solver_name = CBC)


# variables setting

# define integer variables of main courses
M_1 = m.add_var(name = "M_Course_1", var_type = INTEGER, lb = 0) # beef burger
M_2 = m.add_var(name = "M_Course_2", var_type = INTEGER, lb = 0) # pork burger
M_3 = m.add_var(name = "M_Course_3", var_type = INTEGER, lb = 0) # chicken burger
M_4 = m.add_var(name = "M_Course_4", var_type = INTEGER, lb = 0) # fried chicken


# define integer variables of sides
S_1 = m.add_var(name = "Side_1", var_type = INTEGER, lb = 0) # french fried
S_2 = m.add_var(name = "Side_2", var_type = INTEGER, lb = 0) # salted crispy chicken
S_3 = m.add_var(name = "Side_3", var_type = INTEGER, lb = 0) # ice smoothies
S_4 = m.add_var(name = "Side_4", var_type = INTEGER, lb = 0) # salad


# define integer variables of drinks
D_1 = m.add_var(name = "Drink_1", var_type = INTEGER, lb = 0) # cola
D_2 = m.add_var(name = "Drink_2", var_type = INTEGER, lb = 0) # Sprite
D_3 = m.add_var(name = "Drink_3", var_type = INTEGER, lb = 0) # black tea
D_4 = m.add_var(name = "Drink_4", var_type = INTEGER, lb = 0) # green tea


# define integer variables of packages
P_1 = m.add_var(name = "Package_1", var_type = INTEGER, lb = 0) # package of beef burger
P_2 = m.add_var(name = "Package_2", var_type = INTEGER, lb = 0) # package of pork burger 
P_3 = m.add_var(name = "Package_3", var_type = INTEGER, lb = 0) # package of chicken burger
P_4 = m.add_var(name = "Package_4", var_type = INTEGER, lb = 0) # package of chicken
P_5 = m.add_var(name = "Package_5", var_type = INTEGER, lb = 0) # package of party




# constraints setting

# demands of main courses
m += M_1 + P_1 >= 1 # at least 1 beef burger
m += M_3 + P_3 >= 1 # at least 1 chicken burger
m += M_4 + 2*P_4 + 4*P_5 >= 3 # at least 3 fried chicken
m += ( M_1 + M_2 + M_3 + P_1 + P_2 + P_3) >= 4 # at least 4 hamburgers
m += ( M_1 + M_2 + M_3 + M_4 + P_1 + P_2 + P_3 + 2*P_4 + 4*P_5 ) >= 8 # at least 8 main courses


# demands of sides
m += S_1 + P_1 + 3*P_5 >= 5 # at east 5 french fried
m += S_2 + P_2 >= 1 # at least 1 salted crispy chicken
m += S_3 + P_3 + 3*P_5 >= 4 # at least 4 ice smoothies
m += S_4 + P_4 >= 2 # at least 2 salad
m += ( S_1 + S_2 + S_3 + S_4 + P_1 + P_2 + P_3 + P_4 + 6*P_5 ) >= 13 # at least 8 sides


# demands of drinks
m += D_1 + P_1 + 4*P_5 >= 2 # at least 2 cola
m += D_2 + P_2 >= 2 # at least 2 Spirite
m += D_3 + P_3 >= 1 # at least 1 black tea
m += ( D_1 + D_2 + D_3 + D_4 + P_1 + P_2 + P_3 + P_4 + 4*P_5 ) >= 6 # at least 6 drinks


# not much waste
m += ( M_1 + M_2 + M_3 + M_4 + P_1 + P_2 + P_3 + 2*P_4 + 4*P_5 ) <= 9 # no more than (9-1) waste main course
m += ( S_1 + S_2 + S_3 + S_4 + P_1 + P_2 + P_3 +   P_4 + 6*P_5 ) <= 16 # no more than (16-8) waste sides
m += ( D_1 + D_2 + D_3 + D_4 + P_1 + P_2 + P_3 +   P_4 + 4*P_5 ) <= 8 # no more than (8-6) drinks




# define goal function
m.objective = ( 150*P_1 + 130*P_2 + 140*P_3 + 150*P_4 + 200*P_5) + \
              ( 120*M_1 + 100*M_2 + 110*M_3 +  60*M_4 ) + \
              (  55*S_1 +  60*S_2 +  45*S_3 +  50*S_4 ) + \
              (  30*D_1 +  30*D_2 +  25*D_3 +  25*D_4 )




# set the parameters of python MIP solver
status = m.optimize(max_seconds = 300)


# solve and return the optimal value
if status == OptimizationStatus.OPTIMAL:    
    print('optimal solution cost {} found'.format(m.objective_value))
    
elif status == OptimizationStatus.FEASIBLE:
    print('sol.cost {} found, best possible: {}'.format(m.objective_value, m.objective_bound))
    
elif status == OptimizationStatus.NO_SOLUTION_FOUND:
    print('no feasible solution found, lower bound is: {}'.format(m.objective_bound))
    


# solve and return the resluts of all variables
if status == OptimizationStatus.OPTIMAL or status == OptimizationStatus.FEASIBLE:
    print('solution:')
    for v in m.vars:
       if abs(v.x) > 1e-6: # only printing non-zeros
          print('{} : {}'.format(v.name, v.x))
