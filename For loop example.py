hii={"gabbar":"good","god":"permission"}
for k,v in hii.items():
    print(k,v)
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)
for i,v in enumerate({'tic','tac','toe'}):
    print(i,v)

for i, v in enumerate({'tic', 'tac', 'toe'}):
    print(i, v)
questions = ["name","quest","color"]
answer = ["harsh","good","blue"]
for q,a in zip(question,answers):
    print("what is your {0}?")
    
    
    
    
#Assignment loop pattern questions



#1
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print(" ")
for x in range(1,5):
    for j in range(1,x+1):
        print(" ",end=" ")
    for k in range(5,x,-1):
         print("*",end=" ")
    print(" ")

print(" ")





#2
a = 5
k = a - 2
for i in range(a, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
k = 2 * a - 2
for i in range(0, a+1):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
print(" ")








#3
a = 5
k = 2 * a - 2
for i in range(0, a):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
k = a - 2
for i in range(a, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
print(" ")






#4
n = 7
a = []
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1, i):
        a[i].append(a[i - 1][j - 1] + a[i - 1][j])
    if (n != 0):
        a[i].append(1)
for i in range(n):
    print("" * (n - i), end=" ", sep=" ")
    for j in range(0, i + 1):
        print('{0:6}'.format(a[i][j]), end=" ", sep=" ")
    print()
    
    
    
    
    
    
    
    
#5
for i in range(1,7):
    for j in range(1,7-i):
        print("", end=" ")
    for k in range (1,i+1):
        print(chr(64+k),end=" ")
    print(" ")
x=71
for i in range(1, 6):
    for j in range(1,i+1):
        print("", end=" ")
    for l in range(6,i,-1):
        print(chr(x),end=" ")
        x+=1
    print("")
    
    
    
    
    
    
    
#6
for i in range(8,1,-1):
    for k in range(1,i):
        print(chr(64+k),end=" ")
    for l in range(8,i,-1):
        print(" ",end=" ")
    for z in range(7, i, -1):
        print(" ", end=" ")
    for j in range(i-1,0,-1):
        if(chr(64+j)=="G"):
            continue
        print(chr(64+j),end=" ")
    print(" ")
    
    
    
    
    
    
    
    
    
    
    
#7
for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end=" ")
    for k in range (1,i+1):
        print(chr(64+k),end=" ")
    for l in range(i,1,-1):
        print(chr(63+l), end=" ")
    print("")
    
    
    
    
    
    
    
    
#8
n = 5
a = []
for i in range(n):
  a.append([])
  a[i].append(1)
  for j in range(1, i):
    a[i].append(a[i - 1][j - 1] + a[i - 1][j])
  if(n != 0):
    a[i].append(1)
for i in range(n):
  print("   " * (n - i), end = " ", sep = " ")
  for j in range(0, i + 1):
    print('{0:6}'.format(a[i][j]), end = " ", sep = " ")
  print()
