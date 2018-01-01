#__author: elzhang
#date: 2018/1/1


_user ="alex"
_passwd = "abc123"

for i in range(3):
    username = input("Username:")
    password = input("Password:")
    if username == _user and password == _passwd :
        print("Welcome %s login...." % _user)
        break #跳出，中断
    else:
        print("Invalid username or password !")
else:
    print("要不要脸，臭流氓啊，小虎。")