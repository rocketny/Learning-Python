# Ch1 准备知识
## 一、网络
>However, a web browser is just code, and
code can be taken apart, broken into its basic components, rewritten, reused, and
made to do anything you want.

（上面这段话来自《Web Scraping with Python》，你可以很轻松找地在互联网上找到它的电子版（甚至是中文版），笔者主要参考的也是这本书.）

—— 


  上面这段话向我们抛出一个问题，如何用Python实现浏览器的功能？  
  这里我们并不要求浏览器的所有功能，只要求它的最基本的功能——从互联网上获得数据.可以采取下面的代码实现：

```python
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')

print(html.read())
```

  保存并在powershell里运行这段代码，就能获得网址[http://pythonscraping.com/pages/page1.html](http://pythonscraping.com/pages/page1.html)
这一网页的全部HTML代码.更为准确的说，他会返回域名http://pythonscraping.com/pages/page1.html 下pages目录中的pages.html文件  

  urllib库是一个标准库（Python自带的库）无需额外下载，其中的urlopen函数，即能远程打开、读取一个互联网上的对象，除了像这里用来打开HTML文件，
还可以用来打开图像等，我们会在此后频繁的使用这个函数.

## 二、BeautifulSoup库简介
### 1.安装BeautifulSoup库
  我强烈建议你直接下载Anoconda，而非Python的原始版本.因为前者已经集成很多十分常用的库（例如numpy、BeautifulSoup等）.
Anoconda的下载、安装和设置可以到  
[https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/assignments/)
下载Problem Set0,参考里面的Getting_Start.pdf.


  若你不想使用Anoconda，则可以以管理员身法打开命令提示符（在开始菜单输入cmd搜索），然后输入

```
pip install beautifulsoup4
```

之后在idle中输入

```
from bs4 import BeautifulSoup
```

如果没有报错则安装成功.
需要注意的是，笔者并不清楚这一安装是否会受限，如果安装不成功可以在科学上网后再尝试.





### 2.BeautifulSoup库的作用与使用
  BeautifulSoup库的作用在于能够将urlopen所得的对象转换成BeautifulSoup对象，看下面的代码：
  
```python
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
```

上面的代码在引入两个库后，首先得到网页中的html文件，而后根据得到的对象创建了一个BeautifulSoup对象.  
而BeautifulSoup对象是结构化的，这就很方便我们提取html文件中的信息.  

最后一行的代码就帮助我们显示出其h1的内容.  

这里，我们使用Beautiful创建bs时，使用了两个参数，其中的第二个参数是指明使用何种解析器（parser），一般不同的解析器的输出差异不大.  
中文版的教程只介绍了这一种解析器，而在英文版教程中还介绍了 lxml 和 html5lib 这两种解析器，他们的有点都是可以帮助处理不太“良好”的html文件，缺点是必须从外部下载后才能使用（pip）


### 3.异常处理
&ensp;&ensp;在中文版的教程中，这一部分叫做可靠的网络链接，笔者认为是不合适的，整个这一部分几乎都在阐述如何使用在爬虫时使用异常捕捉  
这是因为在爬虫时，我们往往需要爬取大量的数据，经常会运行代码后就去睡觉了或者干其他事了，如果不使用异常捕捉，则我们原本预想的回到电脑前就会得到
所需要的数据的梦想往往就会变成一个异常提示.

请看下面的代码：

```python
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
```

上面的代码中，我们几乎在每个可能出现异常的地方都进行了异常捕捉.








