'''
描述
'三位水仙花数'是指一个三位整数，其各位数字的3次方和等于该书本身。
例如：ABC是一个'三位水仙花数'，则：A的三次方 + B的三次方 + C的三次方 = ABC
请按照从小到大的顺序输出所有的三位水仙花数，请用'逗号'分隔输出结果。
注意：这是一个OJ题目，输出格式要严格一致。

输入
无
输出
示例：634,412
(注意,这两个数字不是水仙花数)
'''
# 三位水仙花数 Narcissistic_number.py
Num = []
for i in range(100,1000):
  A = i//100
  B = (i//10%10)
  C = i%10
  if pow(A,3) + pow(B,3) + pow(C,3) == i:
    Num.append(i)
  else:
    continue

print(",".join(str(i) for i in Num))
