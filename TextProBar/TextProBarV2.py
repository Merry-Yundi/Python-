#TextProBarV2.py
import time # 导入time库
for i in range(101): 
    print("\r{:3}%".format(i), end="") # end=""print()参数，表示不换行；\r 加在字符串最前面表示回到字符串首位；格式化百分比
    time.sleep(0.1)
