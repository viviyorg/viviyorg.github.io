
###Python手机自动化工具桌面按键

第三方库 uiautomator＋调试工具 atx wedit，


https://developer.android.google.cn/training/testing/ui-automator?hl=zh-cn，UI Automator  |  Android 开发者  |  Android Developers，UiAutomator是谷歌在Android4.1版本发布时推出的一款用Java编写的UI测试框架，由一个名为Xiaocong He的大牛将这个想法实现了出来，实现原理是在手机上运行了一个http rpc服务，将uiautomator中的功能开放出来，然后再将这些http接口封装成Python库。GitHub项目地址：https://github.com/xiaocong/uiautomator.git
但由于xiaocong/uiautomator这个库，已经很久不见更新。因此在这个库的基础上，又重新诞生了另外一个加强版本，为了方便做区分原作者在后面加了个2 名为：openatx/uiautomator2，GitHub项目地址：https://github.com/openatx/uiautomator2.git
https://pypi.org/project/uiautomator/，uiautomator · PyPI
https://blog.csdn.net/m0_60126160/article/details/119087945，uiautomator2自动化测试框架
https://blog.csdn.net/kong_gu_you_lan/article/details/77197944，https://github.com/alidili/Demos/tree/master/UiAutomatorDemo，自动化测试工具UiAutomator使用详解

https://github.com/openatx/atxserver2，atxserver2

vscode结合miniconda来编写python，和pycharm的区别，https://youtu.be/3Dyvi0HkdOI
python按键基础，用python调用windows api来实现简单的桌面按键功能，https://youtu.be/0Jzpk1JgDMA，讲LUA按键的时候因为要下载手机按键精灵但是有人电脑是mac没有对应版本，

pycharm下载：https://www.jetbrains.com/pycharm/dow...
vscode下载：https://code.visualstudio.com/
miniconda下载：https://docs.conda.io/en/latest/miniconda.html，Miniconda — Conda documentation
miniconda安装：https://blog.csdn.net/weixin_54227557...，windows安装miniconda_irrationality的博客-CSDN博客_windows安装miniconda
pyautogui中文文档：https://github.com/asweigart/pyautogu...，PyAutoGUI——让所有GUI都自动化
http://www.4399.com/flash/154247_3.htm，别再踩白块了_别再踩白块了html5游戏在线玩_4399h5游戏-4399在线玩

可从程序Anaconda3打开Anaconda Prompt(Anaconda3)命令行环境，查看环境列表conda env list，也可以在PyCharm选择环境Interpreter，
PyCharm中打开Setting--Project：>Python Interpreter，点击+，查找安装包模块之后点击Install Pckage安装，或者通过Anaconda Prompt(Anaconda3)命令行环境输入pip install ##安装，或者在PyCarm中Terminal里面cd相关虚拟环境进行安装；
