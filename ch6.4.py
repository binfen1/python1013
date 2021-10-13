import string

passWord = input("密码:")
if len(passWord) < 8:
    print("密码长度不够！")
else:
    yes = [0] * 4
    for ch in passWord:
        if not yes[0] and ch in string.digits:
            yes[0] = 1
        elif not yes[1] and ch in string.ascii_lowercase:
            yes[1] = 1
        elif not yes[2] and ch in string.ascii_uppercase:
            yes[2] = 1
        elif not yes[3] and ch in '+-*<>=&^%':
            yes[3] = 1
    gradeDict = {1: '弱', 2: '较弱', 3: '一般', 4: '强'}
    print(gradeDict.get(sum(yes), 'error'))
