s = input("请输入一个三位数")
n = input(s)


a,b = divmod(s,100)
b,c = divmod(s,10)

print(a,b,c)