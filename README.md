# PlayWright-study
基于python的前端自动化框架实践

## 1、 playwright vs  selenium ?

```bash
# playwright 的优点
1、支持所有浏览器的 Headless 模式和非 Headless 模式的测试
2、自动安装对应的浏览器和驱动，不需要额外配置 WebDriver 
3、提供了自动等待相关的 API,全局使用slow_no 或者 强制等待 page.wait_for_timeout() ，抛弃了selenium的time.sleep()
4、支持两种编写模式，一种是类似 Puppetter 一样的异步模式，另一种是像 Selenium 一样的同步模式
5、运行速度是非常快
6、强大的录制功能，那就是可以playwright codegen录制我们在浏览器中的操作并将代码自动生成出来
7、BrowserContext 是一个类似隐身模式的独立上下文环境，其运行资源是单独隔离的，在做一些自动化测试过程中，每个测试用例我们都可以
单独创建一个 BrowserContext 对象，这样可以保证每个测试用例之间互不干扰
```

### 2、 安装依赖

```bash
1、 需 Python 3.7以上版本。
2、 
	安装 playwright 库：
		pip install playwright -i http://pypi.douban.com/simple --trusted-host pypi.douban.com  
	安装单元测试：
		pip install pytest-playwright -i http://pypi.douban.com/simple --trusted-host pypi.douban.com    
	安装浏览器：
		playwright install  
		
3、	安装：pytest-html、 pytest 
```

## 3、 学习资料

```
	源码： https://github.com/microsoft/playwright-python
	官方文档： https://playwright.dev/python/docs/intro
	国人写的技术文档：https://cuiqingcai.com/36045.html
	谷歌浏览器启动参数： https://blog.csdn.net/bigcarp/article/details/121142873
```

## 4、 本项目介绍

```bash
【playwright-demo】 文件夹里面编写了一些常用方法，元素定位，元素操作等
【playwright-framework】 文件夹是一个基于pytest的PO模式的框架，提供功能分层：
	定位符、页面操作、业务逻辑三层：合并成了 page 类
	测试用例层：test 类（基于 pytest）
	数据层：yaml 文件 （config 数据 与 fixtures 数据）
	结果层：HTML 报告（基于 pytest-html）
```


## 5、其他介绍

### 5.1 Playwrigth 的录制功能

CMD命令行： playwright codegen

比如  -o 代表输出的代码文件的名称；
			-target 代表使用的语言，默认是 python，即会生成同步模式的操作代码，如果传入 python-async 就会生成异步模式的代码
			-b 代表的是使用的浏览器，默认是 Chromium

```bash
如：  playwright codegen -o script.py -b firefox
就弹出了一个 Firefox 浏览器，同时右侧会输出一个脚本窗口，实时显示当前操作对应的代码。
我们可以在浏览器中做任何操作，操作完毕之后，关闭浏览器，Playwright 会生成一个 script.py 文件 ,这个文件可以之间运行。

# 查看帮助
python -m playwright codegen --help
```

### 5.2 待update中...


