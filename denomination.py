#Program to count minimum number of denomination for given amount

print("Please enter the currency you want to know")
x=int(input())
q=[2000,500,200,100,50,20,10,5,2,1]
for i in range(10):
    Q=q[i]
    y=x/Q
    print("Notes of",q[i],"is",y)
    y=x%Q

if x>=2000:
    x = x / 2000
    print("2000 notes are",int(x))
    x=x%2000
if x>=500 and x<2000:
    x = x / 500
    print("500 notes are",int(x))
    x=x%500
if x>=200 and x<500:
    x = x / 200
    print("200 notes are",int(x))
    x=x%200
if x >= 100 and x < 200:
    x = x / 100
    print("100 notes are", int(x))
    x = x % 100
if x >= 50 and x < 100:
    x = x / 100
    print("100 notes are", int(x))
    x = x % 100
if x >= 20 and x < 50:
    x = x / 20
    print("20 notes are", int(x))
    x = x % 20
if x >= 10 and x < 20:
    x = x / 10
    print("10 notes are", int(x))
    x = x % 10
if x >= 5 and x < 10:
    x = x / 5
    print("5 notes are", int(x))
    x = x % 5
if x >= 2 and x < 5:
    x = x / 2
    print("2 notes are", int(x))
    x = x % 2
if x >= 1 and x < 2:
    x = x / 1
    print("1 notes are", int(x))
    x = x % 1
