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

# define integer variables of walking distance of each period
d_10 = m.add_var(name = "dist_10", var_type = INTEGER, lb = 0, ub = 5)
d_11 = m.add_var(name = "dist_11", var_type = INTEGER, lb = 0, ub = 5)
d_12 = m.add_var(name = "dist_12", var_type = INTEGER, lb = 0, ub = 10)
d_13 = m.add_var(name = "dist_13", var_type = INTEGER, lb = 0, ub = 10)
d_14 = m.add_var(name = "dist_14", var_type = INTEGER, lb = 0, ub = 10)

d_20 = m.add_var(name = "dist_20", var_type = INTEGER, lb = 0, ub = 5)
d_21 = m.add_var(name = "dist_21", var_type = INTEGER, lb = 0, ub = 5)
d_22 = m.add_var(name = "dist_22", var_type = INTEGER, lb = 0, ub = 10)
d_23 = m.add_var(name = "dist_23", var_type = INTEGER, lb = 0, ub = 10)
d_24 = m.add_var(name = "dist_24", var_type = INTEGER, lb = 0, ub = 10)

d_30 = m.add_var(name = "dist_30", var_type = INTEGER, lb = 0, ub = 5)
d_31 = m.add_var(name = "dist_31", var_type = INTEGER, lb = 0, ub = 5)
d_32 = m.add_var(name = "dist_32", var_type = INTEGER, lb = 0, ub = 10)
d_33 = m.add_var(name = "dist_33", var_type = INTEGER, lb = 0, ub = 10)
d_34 = m.add_var(name = "dist_34", var_type = INTEGER, lb = 0, ub = 10)

d_40 = m.add_var(name = "dist_40", var_type = INTEGER, lb = 0, ub = 5)
d_41 = m.add_var(name = "dist_41", var_type = INTEGER, lb = 0, ub = 5)
d_42 = m.add_var(name = "dist_42", var_type = INTEGER, lb = 0, ub = 10)
d_43 = m.add_var(name = "dist_43", var_type = INTEGER, lb = 0, ub = 10)
d_44 = m.add_var(name = "dist_44", var_type = INTEGER, lb = 0, ub = 10)

d_50 = m.add_var(name = "dist_50", var_type = INTEGER, lb = 0, ub = 5)
d_51 = m.add_var(name = "dist_51", var_type = INTEGER, lb = 0, ub = 5)
d_52 = m.add_var(name = "dist_52", var_type = INTEGER, lb = 0, ub = 10)
d_53 = m.add_var(name = "dist_53", var_type = INTEGER, lb = 0, ub = 10)
d_54 = m.add_var(name = "dist_54", var_type = INTEGER, lb = 0, ub = 10)

d_60 = m.add_var(name = "dist_60", var_type = INTEGER, lb = 0, ub = 5)
d_61 = m.add_var(name = "dist_61", var_type = INTEGER, lb = 0, ub = 5)
d_62 = m.add_var(name = "dist_62", var_type = INTEGER, lb = 0, ub = 10)
d_63 = m.add_var(name = "dist_63", var_type = INTEGER, lb = 0, ub = 10)
d_64 = m.add_var(name = "dist_64", var_type = INTEGER, lb = 0, ub = 10)

d_70 = m.add_var(name = "dist_70", var_type = INTEGER, lb = 0, ub = 5)
d_71 = m.add_var(name = "dist_71", var_type = INTEGER, lb = 0, ub = 5)
d_72 = m.add_var(name = "dist_72", var_type = INTEGER, lb = 0, ub = 10)
d_73 = m.add_var(name = "dist_73", var_type = INTEGER, lb = 0, ub = 10)
d_74 = m.add_var(name = "dist_74", var_type = INTEGER, lb = 0, ub = 10)





# define binary variables that whether the peddler reach the specific bonus point or not
b_10 = m.add_var(name = "bonus_10", var_type = BINARY)
b_11 = m.add_var(name = "bonus_11", var_type = BINARY)
b_12 = m.add_var(name = "bonus_12", var_type = BINARY)
b_13 = m.add_var(name = "bonus_13", var_type = BINARY)
b_14 = m.add_var(name = "bonus_14", var_type = BINARY)

b_20 = m.add_var(name = "bonus_20", var_type = BINARY)
b_21 = m.add_var(name = "bonus_21", var_type = BINARY)
b_22 = m.add_var(name = "bonus_22", var_type = BINARY)
b_23 = m.add_var(name = "bonus_23", var_type = BINARY)
b_24 = m.add_var(name = "bonus_24", var_type = BINARY)

b_30 = m.add_var(name = "bonus_30", var_type = BINARY)
b_31 = m.add_var(name = "bonus_31", var_type = BINARY)
b_32 = m.add_var(name = "bonus_32", var_type = BINARY)
b_33 = m.add_var(name = "bonus_33", var_type = BINARY)
b_34 = m.add_var(name = "bonus_34", var_type = BINARY)

b_40 = m.add_var(name = "bonus_40", var_type = BINARY)
b_41 = m.add_var(name = "bonus_41", var_type = BINARY)
b_42 = m.add_var(name = "bonus_42", var_type = BINARY)
b_43 = m.add_var(name = "bonus_43", var_type = BINARY)
b_44 = m.add_var(name = "bonus_44", var_type = BINARY)

b_50 = m.add_var(name = "bonus_50", var_type = BINARY)
b_51 = m.add_var(name = "bonus_51", var_type = BINARY)
b_52 = m.add_var(name = "bonus_52", var_type = BINARY)
b_53 = m.add_var(name = "bonus_53", var_type = BINARY)
b_54 = m.add_var(name = "bonus_54", var_type = BINARY)

b_60 = m.add_var(name = "bonus_60", var_type = BINARY)
b_61 = m.add_var(name = "bonus_61", var_type = BINARY)
b_62 = m.add_var(name = "bonus_62", var_type = BINARY)
b_63 = m.add_var(name = "bonus_63", var_type = BINARY)
b_64 = m.add_var(name = "bonus_64", var_type = BINARY)

b_70 = m.add_var(name = "bonus_70", var_type = BINARY)
b_71 = m.add_var(name = "bonus_71", var_type = BINARY)
b_72 = m.add_var(name = "bonus_72", var_type = BINARY)
b_73 = m.add_var(name = "bonus_73", var_type = BINARY)
b_74 = m.add_var(name = "bonus_74", var_type = BINARY)




# define binary variables that whether the peddler would stay and peddle at the specific bonus point or not
p_10 = m.add_var(name = "peddle_10", var_type = BINARY)
p_11 = m.add_var(name = "peddle_11", var_type = BINARY)
p_12 = m.add_var(name = "peddle_12", var_type = BINARY)
p_13 = m.add_var(name = "peddle_13", var_type = BINARY)
p_14 = m.add_var(name = "peddle_14", var_type = BINARY)

p_20 = m.add_var(name = "peddle_20", var_type = BINARY)
p_21 = m.add_var(name = "peddle_21", var_type = BINARY)
p_22 = m.add_var(name = "peddle_22", var_type = BINARY)
p_23 = m.add_var(name = "peddle_23", var_type = BINARY)
p_24 = m.add_var(name = "peddle_24", var_type = BINARY)

p_30 = m.add_var(name = "peddle_30", var_type = BINARY)
p_31 = m.add_var(name = "peddle_31", var_type = BINARY)
p_32 = m.add_var(name = "peddle_32", var_type = BINARY)
p_33 = m.add_var(name = "peddle_33", var_type = BINARY)
p_34 = m.add_var(name = "peddle_34", var_type = BINARY)

p_40 = m.add_var(name = "peddle_40", var_type = BINARY)
p_41 = m.add_var(name = "peddle_41", var_type = BINARY)
p_42 = m.add_var(name = "peddle_42", var_type = BINARY)
p_43 = m.add_var(name = "peddle_43", var_type = BINARY)
p_44 = m.add_var(name = "peddle_44", var_type = BINARY)

p_50 = m.add_var(name = "peddle_50", var_type = BINARY)
p_51 = m.add_var(name = "peddle_51", var_type = BINARY)
p_52 = m.add_var(name = "peddle_52", var_type = BINARY)
p_53 = m.add_var(name = "peddle_53", var_type = BINARY)
p_54 = m.add_var(name = "peddle_54", var_type = BINARY)

p_60 = m.add_var(name = "peddle_60", var_type = BINARY)
p_61 = m.add_var(name = "peddle_61", var_type = BINARY)
p_62 = m.add_var(name = "peddle_62", var_type = BINARY)
p_63 = m.add_var(name = "peddle_63", var_type = BINARY)
p_64 = m.add_var(name = "peddle_64", var_type = BINARY)

p_70 = m.add_var(name = "peddle_70", var_type = BINARY)
p_71 = m.add_var(name = "peddle_71", var_type = BINARY)
p_72 = m.add_var(name = "peddle_72", var_type = BINARY)
p_73 = m.add_var(name = "peddle_73", var_type = BINARY)
p_74 = m.add_var(name = "peddle_74", var_type = BINARY)






# adding constraints

# setting that whether the peddler reach the specific distance point or not
m += (d_10 / 5)  >= b_10
m += (d_11 / 5)  >= b_11
m += (d_12 / 10) >= b_12
m += (d_13 / 10) >= b_13
m += (d_14 / 10) >= b_14

m += (d_20 / 5)  >= b_20
m += (d_21 / 5)  >= b_21
m += (d_22 / 10) >= b_22
m += (d_23 / 10) >= b_23
m += (d_24 / 10) >= b_24

m += (d_30 / 5)  >= b_30
m += (d_31 / 5)  >= b_31
m += (d_32 / 10) >= b_32
m += (d_33 / 10) >= b_33
m += (d_34 / 10) >= b_34

m += (d_40 / 5)  >= b_40
m += (d_41 / 5)  >= b_41
m += (d_42 / 10) >= b_42
m += (d_43 / 10) >= b_43
m += (d_44 / 10) >= b_44

m += (d_50 / 5)  >= b_50
m += (d_51 / 5)  >= b_51
m += (d_52 / 10) >= b_52
m += (d_53 / 10) >= b_53
m += (d_54 / 10) >= b_54

m += (d_60 / 5)  >= b_60
m += (d_61 / 5)  >= b_61
m += (d_62 / 10) >= b_62
m += (d_63 / 10) >= b_63
m += (d_64 / 10) >= b_64

m += (d_70 / 5)  >= b_70
m += (d_71 / 5)  >= b_71
m += (d_72 / 10) >= b_72
m += (d_73 / 10) >= b_73
m += (d_74 / 10) >= b_74



# setting sequence of distance points
m += b_10 >= b_11
m += b_11 >= b_12
m += b_12 >= b_13
m += b_13 >= b_14

m += b_20 >= b_21
m += b_21 >= b_22
m += b_22 >= b_23
m += b_23 >= b_24

m += b_30 >= b_31
m += b_31 >= b_32
m += b_32 >= b_33
m += b_33 >= b_34

m += b_40 >= b_41
m += b_41 >= b_42
m += b_42 >= b_43
m += b_43 >= b_44

m += b_50 >= b_51
m += b_51 >= b_52
m += b_52 >= b_53
m += b_53 >= b_54

m += b_60 >= b_61
m += b_61 >= b_62
m += b_62 >= b_63
m += b_63 >= b_64

m += b_70 >= b_71
m += b_71 >= b_72
m += b_72 >= b_73
m += b_73 >= b_74



# setting that whether the peddler would stay and peddle at the specific bonus point or not
m += b_10 >= p_10
m += b_11 >= p_11
m += b_12 >= p_12
m += b_13 >= p_13
m += b_14 >= p_14

m += b_20 >= p_20
m += b_21 >= p_21
m += b_22 >= p_22
m += b_23 >= p_23
m += b_24 >= p_24

m += b_30 >= p_30
m += b_31 >= p_31
m += b_32 >= p_32
m += b_33 >= p_33
m += b_34 >= p_34

m += b_40 >= p_40
m += b_41 >= p_41
m += b_42 >= p_42
m += b_43 >= p_43
m += b_44 >= p_44

m += b_50 >= p_50
m += b_51 >= p_51
m += b_52 >= p_52
m += b_53 >= p_53
m += b_54 >= p_54

m += b_60 >= p_60
m += b_61 >= p_61
m += b_62 >= p_62
m += b_63 >= p_63
m += b_64 >= p_64

m += b_70 >= p_70
m += b_71 >= p_71
m += b_72 >= p_72
m += b_73 >= p_73
m += b_74 >= p_74





m += 20*( d_10 + d_11 + d_12 + d_13 + d_14 ) + \
     20*( d_20 + d_21 + d_22 + d_23 + d_24 ) + \
     20*( d_30 + d_31 + d_32 + d_33 + d_34 ) + \
     20*( d_40 + d_41 + d_42 + d_43 + d_44 ) + \
     20*( d_50 + d_51 + d_52 + d_53 + d_54 ) + \
     20*( d_60 + d_61 + d_62 + d_63 + d_64 ) + \
     20*( d_70 + d_71 + d_72 + d_73 + d_74 ) + \
     20*b_10 + 40*b_11 + 60*(b_12 + b_13 + b_14 ) + \
     20*b_20 + 40*b_21 + 60*(b_22 + b_23 + b_24 ) + \
     20*b_30 + 40*b_31 + 60*(b_32 + b_33 + b_34 ) + \
     20*b_40 + 40*b_41 + 60*(b_42 + b_43 + b_44 ) + \
     20*b_50 + 40*b_51 + 60*(b_52 + b_53 + b_54 ) + \
     20*b_60 + 40*b_61 + 60*(b_62 + b_63 + b_64 ) + \
     20*b_70 + 40*b_71 + 60*(b_72 + b_73 + b_74 ) + \
     (60-20)*p_10 + (120-40)*p_11 + (300-60)*(p_12 + p_13) + (360-60)*p_14 + \
     (60-20)*p_20 + (120-40)*p_21 + (300-60)*(p_22 + p_23) + (360-60)*p_24 + \
     (60-20)*p_30 + (120-40)*p_31 + (300-60)*(p_32 + p_33) + (360-60)*p_34 + \
     (60-20)*p_40 + (120-40)*p_41 + (300-60)*(p_42 + p_43) + (360-60)*p_44 + \
     (60-20)*p_50 + (120-40)*p_51 + (300-60)*(p_52 + p_53) + (360-60)*p_54 + \
     (60-20)*p_60 + (120-40)*p_61 + (300-60)*(p_62 + p_63) + (360-60)*p_64 + \
     (60-20)*p_70 + (120-40)*p_71 + (300-60)*(p_72 + p_73) + (360-60)*p_74   \
     >= 10000


    
m.objective = ( 5*(d_10 + d_11) + 10*d_12 + 15*d_13 + 20*d_14 ) + \
              ( 5*(d_20 + d_21) + 10*d_22 + 15*d_23 + 20*d_24 ) + \
              ( 5*(d_30 + d_31) + 10*d_32 + 15*d_33 + 20*d_34 ) + \
              ( 5*(d_40 + d_41) + 10*d_42 + 15*d_43 + 20*d_44 ) + \
              ( 5*(d_50 + d_51) + 10*d_52 + 15*d_53 + 20*d_54 ) + \
              ( 5*(d_60 + d_61) + 10*d_62 + 15*d_63 + 20*d_64 ) + \
              ( 5*(d_70 + d_71) + 10*d_72 + 15*d_73 + 20*d_74 ) + \
              ( 20*p_10 + 40*p_11 + 100*(p_12 + p_13) + 120*p_14) +\
              ( 20*p_20 + 40*p_21 + 100*(p_22 + p_23) + 120*p_24) +\
              ( 20*p_30 + 40*p_31 + 100*(p_32 + p_33) + 120*p_34) +\
              ( 20*p_40 + 40*p_41 + 100*(p_42 + p_43) + 120*p_44) +\
              ( 20*p_50 + 40*p_51 + 100*(p_52 + p_53) + 120*p_54) +\
              ( 20*p_60 + 40*p_61 + 100*(p_62 + p_63) + 120*p_64) +\
              ( 20*p_70 + 40*p_71 + 100*(p_72 + p_73) + 120*p_74)




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
