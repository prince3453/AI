def pour(jug1, jug2,max1,max2,fill):
    #max1, max2, fill = 7,5,4  #Change maximum capacity and final capacity
    print("%d\t%d" % (jug1, jug2))
    if jug2 is fill:
        print("%d\t%d" % (jug2,jug1))
        return
        
    elif jug2 is max2:
        pour(0, jug1,max1,max2,fill)
    elif jug1 != 0 and jug2 is 0:
        b=jug1-max2
        pour(b,max2,max1,max2,fill)
    elif jug1 is fill:
        pour(jug1, 0,max1,max2,fill)
    elif jug1 < max1:
        pour(max1, jug2,max1,max2,fill)
    elif jug1 < (max2-jug2):
        pour(0, (jug1+jug2),max1,max2,fill)
    else:
        pour(jug1-(max2-jug2), (max2-jug2)+jug2,max1,max2,fill)
   

max1=int(input("Enter max of jug1 : "))
max2=int(input("Enter max of jug2 : "))
fill=int(input("Enter water to fill :"))
print("JUG1\tJUG2")
if max1>max2:
    pour(0,0,max1,max2,fill)
else:
    max1,max2=max2,max1
    pour(0,0,max1,max2,fill)
