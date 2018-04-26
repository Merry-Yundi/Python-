# TextProBarV1.py
import time # 导入time库
scale = 10 # 设定进度条总宽度为10个字符
print("------执行开始------") # 居中打印 "执行开始" 两边用'-'填充
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i/scale)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b)) # 打印进度百分比，a,b，并进行格式化
    time.sleep(0.1) # 程序休眠 0.1s
print("------执行结束------") # 居中打印 "执行开始" 两边用'-'填充

