# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class DushuComPipeline(object):
    #def process_item(self, item, spider):
        #return item

        
#from scrapy import signals  
#import json  
#import codecs  
#import sys  
#reload(sys)  
#sys.setdefaultencoding("utf-8")

class QQNewsPipeline(object):
    def process_item(self, item, spider):
        #print("123456")
        #print(item['title'])
        if not item['title']:
            return item
        file_name = item['title'][0] + ".txt"
        fp = open("D://dushu_com//dushu_com//data//"+file_name, 'w')  
        fp.write(item['content'])  
        fp.close()

        return item

