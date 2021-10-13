
sum = 0
print("程序开始运行，开始寻找水仙花数:")
for x in range(100, 1000):
    low = x % 10  # 取余数即最低位的数
    high = x // 100
    middle = (x // 10) % 10
    sum = low ** 3 + high ** 3 + middle ** 3
    if sum == x:
        print(x)

print("程序运行结束!")

