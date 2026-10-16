name ='jalaja'
print(type(name))
#type(value) is a built-in function , its output is types 
# it returns the data type of a value , so you know what kind of object it is 
age= 20
age=str(age)
print(type(age))
# print('your age is '+ age)#this was before age was passed as a string 
#    print('your age is '+ age)
 #TypeError: can only concatenate str (not "int") to str
print('your age is ' +  str(age))
# python is flexible with data types but when you chang a value's type 
# it will treat it as mentioned .

