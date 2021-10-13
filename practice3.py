import math
a = int(input("a="))
s = str(a)
b,c = map(int,input("b,c=").split(','))
d = math.sqrt(b**2-4*a*c)
print("a,b,c=",a,b,c)
print("十进制%d,转换为十六进制=%x,看作十六进制=%u"%(a,a,int(s,16)))
print("sqrt(b**2-4*a*c)=%6.2f"%d)