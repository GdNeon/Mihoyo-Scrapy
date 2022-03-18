import scrapy
import sys
sys.path.append('D:/juese/juese')
from items import JueseItem

class JueseSpider(scrapy.Spider):
    name = 'juese'
    allowed_domains = ["mihoyo.com"]
    start_urls = ['https://bbs.mihoyo.com/ys/obc/content/90/detail?bbs_presentation_style=no_header&tdsourcetag=s_pctim_aiomsg']
    def parse(self,response):
        item = JueseItem()
        hrefs = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[2]/div/div/div/div[3]/div/table/tbody/tr/td[1]/a/@href").extract()
        for href in hrefs:
            href = "https://bbs.mihoyo.com" + href
            yield scrapy.Request(href, callback=self.new_parse, meta={'item':item})

    def new_parse(self,response):
        item = response.meta['item']
        item['name'] = response.xpath("//*[@id='__layout']/div/div[2]/nav/h1/text()")[0].extract()
        item['hp_1'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[1]/table/tbody[2]/tr[2]/td[2]/div/span/text()")[0].extract()
        item['attack_1'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[1]/table/tbody[2]/tr[3]/td[2]/div/span/text()")[0].extract()
        item['defend_1'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[1]/table/tbody[2]/tr[4]/td[2]/div/span/text()")[0].extract()
        item['hp_20'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[2]/table/tbody[2]/tr[3]/td[2]/div/span/text()")[0].extract()
        item['attack_20'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[2]/table/tbody[2]/tr[5]/td[2]/div/span/text()")[0].extract()
        item['defend_20'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[2]/table/tbody[2]/tr[3]/td[4]/div/span/text()")[0].extract()
        item['hp_40'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[3]/table/tbody[2]/tr[2]/td[2]/div/span/text()")[0].extract()
        item['attack_40'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[3]/table/tbody[2]/tr[4]/td[2]/div/span/text()")[0].extract()
        item['defend_40'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[3]/table/tbody[2]/tr[2]/td[4]/div/span/text()")[0].extract()
        item['hp_50'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[4]/table/tbody[2]/tr[2]/td[2]/div/span/text()")[0].extract()
        item['attack_50'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[4]/table/tbody[2]/tr[4]/td[2]/div/span/text()")[0].extract()
        item['defend_50'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[4]/table/tbody[2]/tr[2]/td[4]/div/span/text()")[0].extract()
        item['hp_60'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[5]/table/tbody[2]/tr[3]/td[2]/div/span/text()")[0].extract()
        item['attack_60'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[5]/table/tbody[2]/tr[5]/td[2]/div/span/text()")[0].extract()
        item['defend_60'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[5]/table/tbody[2]/tr[3]/td[4]/div/span/text()")[0].extract()
        item['hp_70'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[6]/table/tbody[2]/tr[2]/td[2]/div/span/text()")[0].extract()
        item['attack_70'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[6]/table/tbody[2]/tr[4]/td[2]/div/span/text()")[0].extract()
        item['defend_70'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[6]/table/tbody[2]/tr[2]/td[4]/div/span/text()")[0].extract()
        item['hp_80'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[7]/table/tbody[2]/tr[2]/td[2]/div/span/text()")[0].extract()
        item['attack_80'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[7]/table/tbody[2]/tr[4]/td[2]/div/span/text()")[0].extract()
        item['defend_80'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[7]/table/tbody[2]/tr[2]/td[4]/div/span/text()")[0].extract()
        item['hp_90'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[8]/table/tbody[2]/tr[1]/td[2]/div/span/text()")[0].extract()
        item['attack_90'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[8]/table/tbody[2]/tr[2]/td[2]/div/span/text()")[0].extract()
        item['defend_90'] = response.xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/div[3]/div[3]/div[1]/div[2]/div/ul[2]/li[8]/table/tbody[2]/tr[1]/td[4]/div/span/text()")[0].extract()
        yield item



