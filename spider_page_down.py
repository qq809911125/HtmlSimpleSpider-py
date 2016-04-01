# coding:utf-8
'''
@网页下载器 ： 将互联网上URL对应的网页下载到本地
目的 ：  将网页下载到本地进行后续的处理及分析
@功能 ：
-1. 可将URL对应的网页以HTML 存储到本地文件或内存字符串
@Python 有几种网页下载器 ？： urllib2 (Python 官方基础模块), requests(第三方包功能更为强大)
@urllib2 网页下载器实现方式：
@-1. urlib2 下载网页方法1：最简单的方法 - >urllib2.urlopen(url)
->例1:
import urllib2　＃载入urllib2 模块

response = urllib2.urlopen('http://www.baidu.com')　  # 发送网页下载请求

print response.getcode()      # 获取状态码，如果是200表示获取成功

cont = response.read()         # read() 方法读取内容

===============================================================================
@-2. urlib2 下载网页方法2： 添加　data  , http header
->例2:
import urllib2　＃载入urllib2 模块

request = urllib2.Request(url)　  # 创建Request对象

request.add_data( 'a' , '1' )      # 添加数据

request.add_header( 'User-Agent' , 'Mozilla/5.0' )         # 添加http的header

response = urllib2.urlopen('http://www.baidu.com')　  # 发送网页下载请求

===============================================================================
@-3. urlib2 下载网页方法3： 添加特殊情景的处理器
场景：
HTTPcookieProcessor    -> 获取需要用户登陆的网站时，对cookie的处理的方法
ProxyHandler   -> 获取需要代理访问的网站时
HTTPSHandler   -> 网站访问协议为加密的HTTPS 时
HTTPRedirectHandler  ->  网页是相互自动的跳转关系时
设定场景后传给 urllib2.build_opener(handler) 然后给urllib2 install 这个opner

->例３:【HTTPcookieProcessor场景】
import urllib2, cookielib　＃载入urllib2 模块

cj = cookielib.CookieJar()    # 创建cookie容器

opener = urllib2.biuld_opener(urlib2.HTTPcookieProcessor(cj))   # 创建1个opener

urllib2.install_opener(opener)    #给urllib2 安装 opener

response = urllib2.urlopen('http://www.baidu.com')　  # 发送网页下载请求,可以请求url或request
==================================================================================
import urllib2,cookielib
url = 'http://www.baidu.com'

print '第一种方法'
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print '第二种方法'

request = urllib2.Request(url)
request.add_header( 'user-agent','Mozilla/5.0' )
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())


print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(request)
print response3.getcode()
print cj
print (response3.read())
'''
import urllib2

class HtmlDownloader(object):
    
    
    def download(self , url): #参数为要下载的URL
        if url is None:# 如果url 为None , 返回None
            return None
        
        response = urllib2.urlopen(url)# 否则 使用urlopen方法打开url
        
        if response.getcode() != 200:#　判断打开的代码是否为200,不是200的话为打开失败
            return None
        
        return response.read()# 返回下载好的内容
    
    



