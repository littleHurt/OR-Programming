import docplex.cp.model as cp

# create initial model
model = cp.CpoModel(name="party")


# define variables
# ----------------------------------------------------------------------------
num_main_courses = 4
num_sides = 4
num_drinks = 4
num_packages = 5

# define integer variables of main courses (m)
# for range(0,4) as {beef burger, pork burger, chicken burger, fried chicken}
listvar_m = model.integer_var_list(num_main_courses, name='main_courses', min=0)

# define integer variables of sides
# for range(0,4) as {french fried, salted crispy chicken, ice smoothies, salad}
listvar_s = model.integer_var_list(num_sides, name='sides', min=0)

# define integer variables of drinks
# for range(0,4) as {french fried, salted crispy chicken, ice smoothies, salad}
listvar_d = model.integer_var_list(num_drinks, name='drinks', min=0)

# define integer variables of packages
# for range(0,5) as {package of beef burger, package of pork burger, package of chicken burger, package of chicken, package of party}
listvar_p = model.integer_var_list(num_packages, name='packages', min=0)
# ----------------------------------------------------------------------------
# End of defining variables





# constraints setting (demands of main courses)
# ----------------------------------------------------------------------------

# at least 1 beef burger
model.add( listvar_m[0] + listvar_p[0] >= 1 )

# at least 1 chicken burger
model.add( listvar_m[2] + listvar_p[2] >= 1 )

# at least 3 fried chicken
model.add( listvar_m[3] + 2*listvar_p[3] + 4*listvar_p[4] >= 3 )

# at least 4 hamburgers
model.add( model.sum(listvar_m[:3] + listvar_p[:3]) >= 4 )

# at least 8 main courses
model.add( model.sum(listvar_m + listvar_p) +
           (2-1)*listvar_p[3] + (4-1)*listvar_p[4] >= 8)
# ----------------------------------------------------------------------------
# End of constraints setting (demands of main courses)





# constraints setting (demands of sides)
# ----------------------------------------------------------------------------

# at east 5 french fried
model.add( listvar_s[0] + listvar_p[0] + 3*listvar_p[4] >= 5 )

# at least 1 salted crispy chicken
model.add( listvar_s[1] + listvar_p[1] >= 1 )

# at least 4 ice smoothies
model.add( listvar_s[2] + listvar_p[2] + 3*listvar_p[4] >= 4 )

# at least 2 salad
model.add( listvar_s[3] + listvar_p[3] >= 2 )

# at least 8 sides
model.add( model.sum(listvar_s + listvar_p) + (6-1)*listvar_p[4] >= 13 )
# ----------------------------------------------------------------------------
# End of constraints setting (demands of sides)




# constraints setting (demands of drinks)
# ----------------------------------------------------------------------------

# at least 2 cola
model.add( listvar_d[0] + listvar_p[0] + 4*listvar_p[4] >= 2 )

# at least 2 Spirite
model.add( listvar_d[1] + listvar_p[1] >= 2 )

# at least 1 black tea
model.add( listvar_d[2] + listvar_p[2] >= 1 )

# at least 6 drinks
model.add( model.sum(listvar_d + listvar_p) + (4-1)*listvar_p[4] >= 6 )
# ----------------------------------------------------------------------------
# End of constraints setting (demands of drinks)




# define objective function
# ----------------------------------------------------------------------------

# define list of cost
list_cost_p = [150,130,140,150,200]
list_cost_m = [120,100,110, 60]
list_cost_s = [55 ,60, 45, 50]
list_cost_d = [30 ,30, 25, 25]

# multiply the cost to each item
list_obj_p = []
for p in range(0,num_packages):
    list_obj_p.append( list_cost_p[p] * listvar_p[p] )

list_obj_m, list_obj_s, list_obj_d = [],[],[]
for i in range(0,4):
    list_obj_m.append( list_cost_m[i] * listvar_m[i] )
    list_obj_s.append( list_cost_s[i] * listvar_s[i] )
    list_obj_d.append( list_cost_d[i] * listvar_d[i] )

# combine all [cost*variables] in an expression
model.add_constraint(
    model.minimize(
        model.sum(list_obj_p + list_obj_m + list_obj_s + list_obj_d))
    )
# ----------------------------------------------------------------------------
# End of defining objective function



# solve model
model_result = model.solve(TimeLimit = 60)
model_result.write() 
# End
