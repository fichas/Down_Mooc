## Down_Mooc是一个下载超星mooc视频的工具
由于近期疫情的影响 ，超星上面经常出现要排队等待的情况 
所以写了一个小工具 用于批量获取超星课程的视频链接
```python
#本工具基于python编写，依赖requests库
#requests库安装方法:
pip install requests
```
### 使用方法如下
找到你课程的主页，一个形如下方链接格式的网址：
https://mooc1-2.chaoxing.com/course/200029621.html
然后把程序解压，在cmd中运行  
```python
 python mooc.py https://mooc1-2.chaoxing.com/course/200029621.html
```
程序会自动在此目录下生成两个文件：
```c++
output.txt //课程的视频链接，需自行下载
name.bat //将此文件放在视频存放的位置，会把视频的名称自动修正
```
