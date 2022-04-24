import docplex.cp.model as cp

# set initial model
model = cp.CpoModel(name="peddler")


# define variables
# ----------------------------------------------------------------------------
for i in range(1,7+1):
    for j in range(0,4+1):
        
        # define integer variables as walking distance of each period   
        var_dist = 'd_{}'.format(i) + '{}'.format(j)
        if j in [0,1]:
            locals()[var_dist] = cp.integer_var(min=0, max=5, name = var_dist)
        else:
            locals()[var_dist] = cp.integer_var(min=0, max=10, name = var_dist)
            
            
        # define binary variables that whether the peddler reach the specific bonus point or not    
        var_bonus = 'b_{}'.format(i) + '{}'.format(j)
        locals()[var_bonus] = cp.binary_var(name = var_bonus)
        
        
        # define binary variables that whether the peddler would stay and peddle at the specific bonus point or not
        var_peddle = 'p_{}'.format(i) + '{}'.format(j)
        locals()[var_peddle] = cp.binary_var(name = var_peddle)
# ----------------------------------------------------------------------------
# End of denining variables





# adding constraints
# ----------------------------------------------------------------------------
for i in range(1,7+1):
    for j in range(0,4+1):
        
        var_dist = 'd_{}'.format(i) + '{}'.format(j)
        var_bonus = 'b_{}'.format(i) + '{}'.format(j)
        var_peddle = 'p_{}'.format(i) + '{}'.format(j)
        
        # constraints that whether the peddler reach the specific distance point or not
        if j in [0,1]:
            model.add_constraint(  (locals()[var_dist] / 5) >= locals()[var_bonus]  )
        else:
            model.add_constraint(  (locals()[var_dist] /10) >= locals()[var_bonus]  )
        
        
        # constraints that whether the peddler would stay and peddle at the specific bonus point or not
        model.add_constraint(  locals()[var_bonus] >= locals()[var_peddle] )
        
        
    # constraints about sequence of distance points
    for j in range(0,4):
        var_bonus_last = 'b_{}'.format(i) + '{}'.format(j)
        var_bonus_next = 'b_{}'.format(i) + '{}'.format(j+1)
        model.add_constraint(  locals()[var_bonus_last] >= locals()[var_bonus_next]  )



# the peddler have to earn at least $10000 in a week
model.add_constraint((
    20*( d_10 + d_11 + d_12 + d_13 + d_14 ) + \
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
    (60-20)*p_70 + (120-40)*p_71 + (300-60)*(p_72 + p_73) + (360-60)*p_74
    ) >= 10000
        )
# ----------------------------------------------------------------------------
# End of adding constraints





# create objective function of minimization
# ----------------------------------------------------------------------------
model.add_constraint(
    model.minimize(
              ( 5*(d_10 + d_11) + 10*d_12 + 15*d_13 + 20*d_14 ) + \
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
              )
        )
# ----------------------------------------------------------------------------


# solve model
model_result = model.solve(TimeLimit = 90)
model_result.write()
# End
    