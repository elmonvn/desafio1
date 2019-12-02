'''
Created on Nov 20, 2019

@author: elmonvn
'''

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class CarrosUolSpider(CrawlSpider):     
    name = 'carrosuol'    
    start_urls = ['https://www.uol.com.br/carros/ultimas/']    
    rules = (        
        Rule(            
            LinkExtractor(allow='/carros/noticias')        
        ),        
        Rule(            
            LinkExtractor(allow='/carros/noticias',), callback='parse_noticia')    
        )
        
    def parse_noticia(self, response):
        yield {
            'portal': self.name,
            'titulo': response.xpath('//i[@class="custom-title"]/text()').extract_first(),        # título
            'corpo': (response.xpath('string(//div[@class="text"])').get()).strip(),                        # corpo
            'data': (response.xpath('//p[@class="p-author time"]/text()').get().split(' '))[0],        # data
            'autor': response.xpath('//p[@class="p-author"]/text()').get(),    # autor
            'url': response.request.url,                                    # URL
            'tags': response.xpath('//tags').getall()                        # tags
        }
        
        # Salva estatísticas do crawling/scraping
        # self.crawler.stats.get_stats() - crawling stats
        # 
