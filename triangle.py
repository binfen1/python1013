
a,b,c = map(int,input("a,b,c=").split(','))
L = [a,b,c]	#将整数存入列表
L.sort()	#将列表按升序排列
if L[0] + L[1] > L[2]:	#若两边之和大于第三边
    print('YES')	#可构成三角形
else:
    print('NO')

