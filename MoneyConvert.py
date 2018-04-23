# MoneyConvert.py
MoneyStr = input()
if MoneyStr[0:3] == "RMB":
    USD = eval(MoneyStr[3:])/6.78
    print("USD{:.2f}".format(USD))
elif MoneyStr[0:3] == "USD":
    RMB = eval(MoneyStr[3:])*6.78
    print("RMB{:.2f}".format(RMB))
else:
    print("格式错误,请重新输入以USD/RMB开头的货币总数")
