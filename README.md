# Down_Mooc
一个基于 Python3 的超星 mooc 课程内容获取工具，方便离线观看。

### 安装

请安装最新版的Python3，并且使用 `pip` 安装 3 个库：`requests` `BeautifulSoup4` `lxml`

```python
pip install requests BeautifulSoup4 lxml
```

然后[下载最新程序](https://github.com/fichas/Down_Mooc/archive/master.zip)并解压。(也可以使用`git clone https://github.com/fichas/Down_Mooc.git`)

### 使用方法如下

1. ####  mooc.py(无法下载具有权限的课程)

   找到你课程的主页，一个形如下方链接格式的网址：
   https://mooc1-2.chaoxing.com/course/206751495.html
   然后把程序解压，在cmd中运行  

   ```python
    python mooc.py https://mooc1-2.chaoxing.com/course/206751495.html
   ```

   程序会自动在此目录下生成两个文件：

   ```c++
   output.txt //课程的视频链接，需自行下载(有的视频是有权限的，无法下载)
   name.bat //将此文件放在视频存放的位置，会把视频的名称自动修正(有的视频有问题，可能老师的命名方式比较奇怪，先鸽着)
   ```

2. #### mooc_cookie.py(可以下载已选课程中已经开放的章节，需要获取cookies)

   在课程中心，打开想要下载的课程，课程链接形式如下：

   https://mooc1-1.chaoxing.com/mycourse/studentcourse?courseId=1234561234&vc=1&clazzid=12345123&enc=1234567123456123456

   在浏览器中登录后，按 `F12`，在浏览器控制台中执行

   ```javascript
   copy(document.cookie);
   ```

   执行完成后，cookies 会自动复制到粘贴板。

   （也可以 `console.log(document.cookie);` 然后手动复制输出结果。）

   在调用程序获取课程的时候，会自动要求输入 cookies，粘贴便是。

   

   在解压好的目录下，在cmd中运行

   ```python
   python mooc_cookie.py
   ```

   按照相应的提示输入课程链接和cookies就可以获取到课程内容了。

   程序会在当前目录下自动生成

   ```c++
   output.txt //课程的视频链接，需自行下载(可以使用IDM或迅雷等工具自行下载)
   ```



### 特别感谢

[Foair的Course Crawler](https://github.com/Foair/course-crawler)

### 声明

仅限个人学习和研究使用，切勿用于其他用途。

本程序主体功能只是下载课件和附件，无任何手段获得付费课程，也没有以任何方式向任何人收取费用。

如果将程序用于商业用途或其他非法用途，一切后果由用户自负。

### 许可协议

请遵照 MIT 许可使用该程序。