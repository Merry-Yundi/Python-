# TempConvert.py
TempStr = input("请您输入温度及其符号:")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("您需要的摄氏温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = eval(TempStr[0:-1])*1.8 + 32
    print("您需要的华氏温度是{:.2f}F".format(F))
else:
    print("格式错误,请重新输入")
    
