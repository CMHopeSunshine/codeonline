<div align="center">
# 在线运行代码

HoshinoBot在线运行代码插件
</div>

移植自nonebot2插件 [https://github.com/yzyyz1387/nonebot_plugin_code/](https://github.com/yzyyz1387/nonebot_plugin_code/)

##安装
到/hoshino/modules目录下git clone https://github.com/CMHopeSunshine/codeonline
并在/hoshino/config/__bot__.py的MODULES_ON处添加codeonline开启模块

## 指令
```
#code#[语言]#(-i)#(输入)#[代码]
[]为必须，()为可选
-i：可选 输入 后跟输入内容

运行代码示例(python)(无输入)：
    #code#py#
        print("hello world")
        
        输出结果为：hello world
运行代码示例(python)(有输入)：
    #code#py#-i#你好#
        print(input())
        
        输出结果为：你好
        
运行代码示例(python)(生成随机数)：
    #code#py#-i#50,100,3#
        import random
        list=str(input()).split(',')
        p='roll%s个%s到%s以内的数:' % (list[2],list[0],list[1])
        for i in range(0,int(list[2])):
            n=random.randint(int(list[0]),int(list[1]))
            p+=str(n)+' '
        print(p)
        
        输出结果为(例)：roll3个50到100以内的数:86 54 54 
        
```
