# coding:utf-8
'''
@网页解析器 ： 从网页中提取由价值的数据的工具
@功能 : 从网页下载器下载好的 html页面字符串中，提取有价值数据，和新的待爬取的url列表
@Python有哪几种网页解析器
-(1).使用　正则表达式 ->　字符串形式的模糊匹配
-(2).使用　Python 自带的 html.parser 模块　-> 结构化解析
-(3).使用　BeautifulSoup 第三方插件，这个插件可使用html.parser,和 lxml来解析　-> 结构化解析
-(4).使用　lxml 第三方插件 解析 http,xlm网页　-> 结构化解析
--->结构化解析－DOM：将整个网页的文档下载成一个DOM树的形式进行上下级元素的遍历和访问
Beautifulsoup文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc/
@BeautifulSoup使用语法
1. 根据从已下载好的HTML网页的字符串，创建一个BeautifulSoup的对象，创建这个对象的同时
会将整个网页分析成一个DOM树

例:  创建 BeautifulSoup 对象

    # 载入 bs4 下的BeautifulSoup模块
  1 from bs4 import BeautifulSoup  
  2 # 根据html网页字符串创建BeautifulSoup 对象 并传入参数
  3 soup = BeautifulSoup(
  4                                      html_doc ,                         #    HTML文档字符串
  5                                      'html.parser',                     #    设置HTML解析器
  6                                      from_encoding='utf-8'         #    设置HTML文档编码
  7                                        )
                                         
2. 节点的搜索
  根据下载好的html分档字符串分析出的DOM树，就可以对每个节点进行搜索 (使用:find,find_all 方法)
-> find_all 方法 : 会搜索出所有满足要求的节点
-> find　方法 : 会搜索出第一个满足要求的节点
find_all(name,attrs,string)   # 搜索节点 名称，属性 , 文字，find方法使用相同
-> 可传入单一参数，或者多个，如只根据搜索节点名称，或根绝名称和属性进行搜索
(节点是指html 网页内的，如body，div, a , 等标签)
搜索节点时可使用节点的的名称，属性，文字进行搜索
 例：
 soup.find_all('a')   # 搜索全部标签为 a的节点
 soup.find_all('a' , herf=' view/123.html')  # 搜索标签为a ,链接符合' view/123.html'形式的节点
 soup.find_all('a' , herf=re.compile(r'/view/\+d\.html '))  # 也可使用正则表达式    
 # 搜索所有标签为div ,class为'abc',文字为 'Python'的节点,(class_ 加下划线避免关键字冲突)
 soup.find_all('div' , class_= ' abc ' , string = ' Pyhon ' )  
 
3. 访问节点信息
例:
# 假设我们得到了 <a href = '123.html' > Python </a> 这样的节点
node.name        # 获取搜索到的节点的标签名称
node[ ' herf ' ]   #  获取搜索到的a节点的herf 属性
node.get_text() #  获取搜索到的a节点的链接文字
 
 @节点是什么
 例：<a class="reference external" href="http://www.crummy.com/">Beautiful</a>
　　－节点名称　a
         - 属性　class , href
         - 文字　Beautiful
节点的的名称，属性，文字
'''
from bs4 import BeautifulSoup
import re
import urlparse


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):# 分析HTML数据从中获取新的URL
        new_urls = set()# 将遍历出的所有URL保存为列表到内存
        links = soup.find_all('a' , herf=re.compile(r'/view/\d+\.htm'))#获取所有的链接URL
        for link in links:
            new_url = link['herf'] #遍历出所有搜索到的url ,但不完整 (/view/21087.htm)
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls
    
    
    def _get_new_data(self, page_url, soup):# 解析获取 title, (标题,简介 的数据)
        
        res_data = {} # 存放解析出的数据,到字典中
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Pyt<span id="transmark"></span>hon</h1>
        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')# 匹配title的节点
        res_data['title'] = title_node.get_text() # 获取title标签内的文字
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node =soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text() # 获取title标签内的文字
        
        return res_data
    
    
    def parse(self , page_url , html_cont):#提供2个参数,
        if page_url is None or html_cont is None:
            return
        
        soup = BeautifulSoup(html_cont, 'html.parser' , from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)# 创建本地方法
        new_data = self._get_new_data(page_url,soup)# 创建本地方法
        return new_urls , new_data
    
    
    



