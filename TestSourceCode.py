########################################
# TestSourceCode.py
#
# Developed by Shunsuke SAKURAI, Satochi, Yukiho, Yuki
#
# Last update: 13 Jun. 2018
########################################
##############################
# import libraries
##############################
import sys # for getting arguments
import math # for mathematical calculation

##############################
# define functions
##############################
def GetSinAPlusB(_var_a,_var_b):
    var_x = math.sin(_var_a)+ _var_b
    return var_x
   
##############################
# main 
##############################
var_a = float(sys.argv[1])
var_b = float(sys.argv[2])

# calculation
var_x = GetSinAPlus(var_a,var_b)

# show result
print("Sin(A) + B is {}".format(var_x))
