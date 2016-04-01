# coding:utf-8
'''
Created on 2016-3-31

@author: ming
'''


class HtmlOutputer(object):
    def __init__ (self):
        self.datas = []
    
    def collect_data(self , data):# 收集数据的方法
        if data is None:
            return
        self.datas.append(data)

    
    def output_html(self):# 将收集的数据输出到html文件中的方法,
        fout = open('output.html','w')
        
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        
        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
            fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
            fout.write('</tr>')
        
        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')
        
        fout.close()
    
    
    
    


    
    



