#Program to find the day on a particular date

date=input("Enter the date in dd/mm/yyyy format: ")
dd=int(date[0:2])
mm=int(date[3:5])
yyyy=int(date[6:10])-1

def odd(n):
    n=n%7
    return n

qcd=yyyy%400
od=0

#YEARLY ODD DAYS
for i in range(1,qcd+1):
    od+=1
    if i%4==0:
        od+=1
    if i%100==0:
        od-=1

od=odd(od)

#MONTHLY ODD DAYS
def mmod(od,mm,dd,day,i):
    if mm>i:
        od+=day
    elif mm==i:
        od+=dd
    else:
        pass
    return od

yyyy+=1
od=mmod(od,mm,dd,31,1)
if yyyy%4==0:
    if yyyy%100==0:
        if yyyy%400==0:
            od=mmod(od,mm,dd,29,2)
        else:
            od=mmod(od,mm,dd,28,2)
    else:
        od=mmod(od,mm,dd,29,2)
        # pass
else:
    od=mmod(od,mm,dd,28,2)
od=mmod(od,mm,dd,31,3)
od=mmod(od,mm,dd,30,4)
od=mmod(od,mm,dd,31,5)
od=mmod(od,mm,dd,30,6)
od=mmod(od,mm,dd,31,7)
od=mmod(od,mm,dd,31,8)
od=mmod(od,mm,dd,30,9)
od=mmod(od,mm,dd,31,10)
od=mmod(od,mm,dd,30,11)
od=mmod(od,mm,dd,31,12)
od=odd(od)

day=''
if od==0: day='Sunday'
elif od==1: day='Monday'
elif od==2: day='Tuesday'
elif od==3: day='Wednesday'
elif od==4: day='Thursday'
elif od==5: day='Friday'
else: day='Saturday'

#PRINT
print("The day is: ",day)
