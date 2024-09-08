 #1,1,2,3,5,8...
number = 1
last = 0
befor_last = 0
print (number)

for counter in range(0,9):
    before_last=last
    last= number
    number = before_last + last
    print (number)
          
    
 
     
        


