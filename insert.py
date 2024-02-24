#import scrapy, re
#from scrapy.selector import Selector
#from scrapy.http import HtmlResponse


#class insert(scrapy.Spider):
 #   item_id = ''
#    name = 'selected_item_id'
#    start_urls = ['http:/localhost:5000/insertitemdetail']
#    quotation_mark_pattern = re.compile(r'“|”')

#    def parse(self,response):
    
#        selected_item_id = response.xpath('//div[@id="selected_item_id"]')
#        for select_id in selected_item_id:
#            item_id = response.xpath('//section//div[@id="selected_item_id"]/text(').extract_first()
#            return item_id


from flask import request

class insert():
    
    def insertdetails():
        item_id = ''
        item_id = request.form['selected_item_id']
        print(item_id)
        return item_id
        