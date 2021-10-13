
import time , random
t1= time.time()
jok=0
for i in range(0,5):
 n1=random.randint(1,10)
 n2= random.randint(1,10)
 sum=n1+n2
 print( " %d+%d = " %( n1,n2))
 mysum= int( input())
 if(mysum<0):
   break
 elif mysum== sum:
        jok=jok+1
 if (mysum<0):
     print("你中途退出！")
 else:
  t2 = time.time()
  t=float(t2-t1)
  print('5题中，你答对%d题，用时%5.2f秒'%(jok, t))