

import math
print("----计算一元二次方程的根----")
a=input("输入s开始计算:")
try:
    if a.lower() == 's':
        while 1 :
            a = float(input("请输入a的值："))
            b = float(input("请输入b的值："))
            c = float(input("请输入c的值："))
            x1=((-b+math.sqrt(b**2-4*a*c))/(2*a))
            x2=((-b-math.sqrt(b**2-4*a*c))/(2*a))
            print("x1=",x1,"\t","x2=",x2)
            a = input("输入q退出程序！任意键继续。")
            if a.lower() == 'q':
                break
except:
    print("输入的值不符合算术平方根的条件")


