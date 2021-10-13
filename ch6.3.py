from itertools import cycle

sourceStr = input("原字符串：")
result = ''
KeyStr = cycle("encrypt string")
for ch in sourceStr:
    result = result + chr(ord(ch) ^ ord(next(KeyStr)))
print("加密后的字符串：" + result)
