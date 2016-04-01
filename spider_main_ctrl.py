# coding:utf-8
'''
@抓取策略及抓取目标分析
 目标: 
 入口页url:
 URL格式 : 
 数据格式:
 页面编码:
 @
'''
from spider import spider_url_manager, spider_page_down, spider_page_parser,\
    spider_data_output

#　爬虫总调度程序
class SpiderMain(object):
    #初始化各个对象 (构造)
    def __init__(self):
        self.urls = spider_url_manager.UrlManager()# 初始化URL管理器
        self.downloader = spider_page_down.HtmlDownloader()# 初始化HTML下载器
        self.parser = spider_page_parser.HtmlParser()# 初始化HTML解析器
        self.outputer = spider_data_output.HtmlOutputer()# 初始化HTML输出器

    
    def craw(self, root_url):
        count = 1 # 初始爬取次数
        self.urls.add_new_url(root_url) # 将入口URL添加到URL管理器
        while self.urls.has_new_url():# 启动爬虫的循环
            try:
                new_url = self.urls.get_new_url() # 获取一个待爬取的url
                print ' craw %d : %s ' % (count , new_url)# 输出 爬取的次数和链接URL
                html_cont = self.downloader.download(new_url)#获取到待下载的URL后启动HTML下载器下载这个页面,结果储存到 html_cont
                new_urls,new_data = self.parser.parse(new_url,html_cont)#下载好这个网页后使用解析器来解析这个HTML页面,得到新的URL列表及数据
                self.urls.add_new_urls(new_urls)#将解析出的URL添加到URL管理器
                self.outputer.collect_data(new_data)# outputer收集数据
                
                if count == 100:# 爬取100个
                    break
                
                count = count + 1
            except:
                print 'craw failed' #标记URL爬取失败
                
        self.outputer.output_html() # 输出手机好的数据
    
    
    

    
    

if __name__ == "__main__":                                                #  创建主函数main
        root_url = 'http://baike.baidu.com/view/21087.htm'     #  设置爬虫入口地址URL
        obj_spider = SpiderMain()                                            #  创建spidermain 主程序
        obj_spider.craw(root_url)                                            #  使用craw方法启动爬取
