[TOC]

# 前提说明

大数据开发实践课程期末大作业，基于 PyQt5 将股票查询做了一个简单的 GUI demo 版本

# 改进

- GUI 界面，用户体验感更好
- 将可变的部分抽离出来，用户可以自己换数据体验

# 使用

- 操作区域 - 提供更换数据操作和查询、保存、绘制等操作

- 结果区域 - 展示 table 以及 获取的数量等

- 控制台区域 - 显示运行过程中的一些提示信息以及报错信息

# 运行环境

```python
python > 3.7

pip install PyQt5
pip install pyqt5-tools

pip install pyinstaller
```




# 运行方法

- 进入到项目文件夹下,执行 GUI.py 文件

  ![运行方法1](http://qiniu.mengxun.online/20210618020301.png)

- 修改项目目录下GUI.spec中的绝对路径路径 在项目目录下执行 ` pyinstaller -F .\GUI.spec`执行完成后，dist 目录下会生成 exe 可执行文件

- ![运行方法2-1](http://qiniu.mengxun.online/20210618223153.png)

  ![运行方法2-2](http://qiniu.mengxun.online/20210618022401.png)

  ![运行方法2-3](http://qiniu.mengxun.online/20210618020427.png)

- EXE文件网盘链接

  链接：https://pan.baidu.com/s/1j-N5_7vSkN75H_fH1GS6Ng 
  提取码：yhyo 

# 实验截图

## 14.2.1-1

![14.2.1-1](http://qiniu.mengxun.online/20210618012557.png)

## 14.2.1-2

![14.2.1-2](http://qiniu.mengxun.online/20210618012737.png)

## 14.2.2

![14.2.2](http://qiniu.mengxun.online/20210618012921.png)

## 14.2.3

![14.2.3](http://qiniu.mengxun.online/20210618013114.png)

## 14.2.4 & 14.3

![14.2.4 & 14.3](http://qiniu.mengxun.online/20210618013408.png)

## 14.4.1

![14.4.1-1](http://qiniu.mengxun.online/20210618013509.png)

![14.4.1-2](http://qiniu.mengxun.online/20210618013903.png)

## 14.4.2

![14.4.2](http://qiniu.mengxun.online/20210618014310.png)

# 常见错误

- 无网络连接 - 联网

![无网络连接](http://qiniu.mengxun.online/20210618014447.png)

- 股票代码、提供的日期不符合 **tushare** 财经库的数据要求 - 更换其他数据进行尝试

  ![不符合tushare财经库要求](http://qiniu.mengxun.online/20210618014752.png)
