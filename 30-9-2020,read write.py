#1 

f=open("1910093","r") 
print(f.read()) 

 

 

 

#2 

f = open("1910093","a") 
f.write("You are a buddy") 
f.close() 
f=open("1910093","r") 
print(f.read()) 
f.close()
