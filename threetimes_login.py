'''
描述
给用户三次输入用户名和密码的机会，要求如下：
1.如输入第一行输入用户名为‘Kate’，第二行输入密码为‘666666’，输出‘登陆成功！’，退出程序
2.当一共有3次输入用户名或密码不正确输出‘3次用户名或者密码均有误！退出程序。’

输入输出示例
示例1     输入      输出
         Kate     登陆成功！
示例2     输入      输出
         Kate     3次用户名或者密码均有误！退出程序。
         123
         alice
         456
         john
         111111
'''
# 用户登录（三次机会）3times_login.py
login = 0
for i in range(0,3):
  name=input()
  passwd=input()
  if name == "Kate" and passwd == "666666":
    login = 1
    break
if login == 1:
  print("登录成功！")
else:
  print("3次用户名或者密码均有误！退出程序。")
