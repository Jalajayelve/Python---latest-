import os 
#replace()->replacing old value with the new one 
# we have to mention both the values the old one and the new one as well 
price='443483,883'
print(price)
print(price.replace(",","."))

phone ='176-6893-73'
print(phone.replace("-","/"))
print(phone.replace("-"," "))

# convert to real float number 
price = "$1,299.99"
print(price.replace("$","").replace(",",""))

#remove all the characters and 
phonenumber ="+49 (176) 123-4567"
print(phonenumber.replace("+","00").replace("(","").replace(")","").replace("-","").replace(" ",""))

#concatination 
first_name="Jalaja"
last_name="Yelve"
name=first_name+ " "+ last_name
print(name)

#usecase to build file paths - dynamic 
folder=r"C:\Users\Naresh Yelev\OneDrive - Vidyalankar Institute of Technology\23101A0014"
file="agent1_ms_augmented_v2.csv"
full_file_path= folder + "\\"+ file 
print(full_file_path)

#fstring to format and build a string 
name ="jalja"
age =" 21"
print(f"My name is {name}, And age is {age}")

#split value 
stamp = "2026-10-11"
print("My birthdate is " ,stamp.split("-")) 

#MUlTIPLIER 
print(" jalajaa "*3)

#How to extract specific part of our string - INDEXES AND SLICING
#indexing
#extract the first character 
text = "Python" # for positive indexing it counts space as index one as well 
greeting="hello"
print(text [-6])
print(text [0])
#extract the last chracter 
print(text[-1])
print(text[5])

#extract h 
print(text[-3])

#SLICING
date= "2026-09-20"
#extract the year 
print(date[0:4])
print(date[:6])
  