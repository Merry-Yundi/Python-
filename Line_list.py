'''
描述
有一群人站队，没人通过一对整数(h,k)描述
其中h表示人的高度，k表示在此人前面队列中身高不小于此人的总人数
实现一个算法输出这个队列的正确顺序

输入格式
输入格式为而为列表，即list[list[]]形式
外层list包含队列中全部的人，内层list为[h,k]格式，代表个人信息

输出格式
输出格式为：list[list[]]形式
与输出格式一样，需要按照队列顺序排列

输入输出示例

示例1   输入                                     输出
       [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]   [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
'''
# 站队顺序输出 Line_list.py
from operator import itemgetter
queue = eval(input())

queue.sort(key = itemgetter(1))
queue.sort(key = itemgetter(0), reverse = True)

output = []
for item in queue:
    output.insert(item[1], item)
print(output)
