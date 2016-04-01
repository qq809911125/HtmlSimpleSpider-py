# coding:utf-8
'''
@URL 管理器 ： 管理待抓取的URL集合与已抓取的URL集合
--- 目的 ：  防止重复抓取，防止循环抓取
@功能 :
-(1). 添加URL到待爬去集合中
   --> 判断待添加的URL是否在容器中
-(2). 获取容器中待爬取的URL
   -->  判断容器中是否有待爬取的URL
   -->  将URL 从待爬取集合移动到已爬取集合
@url容器实现方式:　【本程序使用内存】
    -1. 内存  ：  Python 内存 -> 待爬取数据库集合， 已爬取数据集合 ： set()
    -2. 关系数据库  :   mysql 为例   urls 表中  以字段  is_crawled     0,1 区分待爬取和已爬取
    -3. 缓存数据库  :   redis 等  -> 待爬取数据库集合， 已爬取数据集合 ：set
'''

class UrlManager(object):
    def __init__(self): # 初始化待爬取的URL列表 和 已爬取的URL列表
        self.new_urls = set() # 初始化待爬取的URL列表
        self.old_urls = set() # 初始化已爬取的URL列表
    
    def add_new_url(self , url): # 向管理器添加单个新的URL
        if url is None: # 对参数进行判断,如果url 为None 
            return       # 不进行添加
        if url not in self.new_urls and url not in self.old_urls:# 如果url 即不在new_urls列表也不在old_urls
            self.new_urls.add(url)# 添加到待爬取列表中
            
 
    def add_new_urls(self , urls):# 向管理器批量添加新的URL
        if urls is None or len(urls) == 0: # 如果 urls 为NONE 或 长度为0
            return #直接返回 不进行添加
        for url in urls:#否则遍历url 
            self.add_new_url(url) # 调用add_new_url 进行单个添加
       
    def has_new_url(self):# 判断管理器中是否有新的待爬取的URL
        return len(self.new_urls) != 0# 如果 self.new_urls 这个列表长度不为0的话,说明有待爬取的URL

    def get_new_url(self):# 从URL管理器获取新的待爬取的URL
        new_url = self.new_urls.pop()# 从待爬取URLS列表中获取一个URL并从其列表中剔除 (pop列表方法)
        self.old_urls.add(new_url)# 加入到已爬取的列表
        return new_url #返回这个获取的URL

    

    

    
    
    
    
    
    
    
    


    



