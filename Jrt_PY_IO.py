# Declare & Assign the variables in python

int_var = 10
float_var = 18.25
string_val = 'ineuron batch2' #or another way "ineuron batch2"
bool_var=True #if we want to assign false, then it should be like False

#function in python for putput
#function does what? They might or might not accept some parameter
print("hello_world")
print ("value of int_var=", int_var, "-result Done")
print ("value of float_var=", float_var, "-result Done")
print ("value of string_val=", string_val, "-result Done")
print ("value of bool_var=", bool_var, "-result Done")

#how to check the data type of any variable
#we can use type()
print("type of int_var?", type(int_var))
print("type of float_var?", type(float_var))
print("type of string_val?", type(string_val))
print("type of bool_var?", type(bool_var))

#how to do the type casting in python??
#int(), float(), str(), bool()
int_var = int_var + 10 # int_var = 10 + 10 and in next stp int_var = 20

casted_int_var = float(int_var)
casted_float_var = int(float_var)

print("Int to Float Typecasting for ", casted_int_var)
print("Int to int Typecasting for ", casted_float_var)

numeric_str = "123"
#numeric_str = numeric_str +50 #is it valid??
#print("value of numeric_str", neumeric_str)

numeric_str = int(numeric_str) + 50
print("value of numeric_str", numeric_str)


#how to take the input on python?
#we can use input function

#name = input()
#age = input()
#print("user name =",name)
#print("user age =",age)

#python file_name.py  ... to execute any python code file

#Another way to take user input
#name = input("Enter the value for name=")
#age = int(input("Enter the value for age="))
#print("user name =",name)
#print("user age =",age)


#print("type of name = ", type(name))
#print("type of age = ", type(age))
