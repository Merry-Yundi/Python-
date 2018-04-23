#PythonDraw.py
import turtle # 引入turtle函数库
turtle.setup(650,350,200,200) # 设定窗体的大小为长650px,宽350px，窗体的左上角位于屏幕左上角的200，200位置
turtle.penup() # 抬起画笔，之后海龟的路径不会出现在画布上;注意最后开始海龟在画布的中心
turtle.fd(-250) # 海龟倒退行进-250px
turtle.pendown() # 将海龟落下，之后的路径显示在画布上
turtle.pensize(25) # 设定当前画笔的宽度为25像素
turtle.pencolor('purple') # 设定当前画笔的颜色为紫色
turtle.seth(-40) # 设定海龟的朝向为绝对-40度方向
for i in range(4):  #
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2) # 最后一个弯曲只有一半
turtle.fd(40) # 让海龟朝前走形成蟒蛇的脖子部分
turtle.circle(16,180) # 设定海龟转向180度
turtle.fd(40*2/3) # 掉头后在爬行一段距离
turtle.done() # 程序运行到这行代码后，窗体不会自动退出


