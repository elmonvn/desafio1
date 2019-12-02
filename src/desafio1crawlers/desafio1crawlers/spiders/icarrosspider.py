'''
Created on Nov 20, 2019

@author: elmonvn
'''

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class ICarrosSpider(CrawlSpider):     
    name = 'icarros'    
    start_urls = ['https://www.icarros.com.br/noticias/arquivo.jsp']    
    rules = (        
        Rule(            
            LinkExtractor(allow='/noticias/arquivo.jsp')        
        ),        
        Rule(            
            LinkExtractor(allow='/noticias/',), callback='parse_noticia')    
        )
        
    def parse_noticia(self, response):
        yield {
            'portal': self.name,
            'titulo': response.xpath('//h1[@class="titulo"]/text()').extract_first(),        # título
            'corpo': (response.xpath('string(//div[@class="ic-box-noticia"])').get()).strip(),                        # corpo
            'data': (response.xpath('//p[@class="dados"]/text()').get().lstrip().split('-'))[0].strip(),        # data
            'autor': ((response.xpath('//p[@class="dados"]/text()').get().lstrip().split('-'))[1].split('/'))[0].strip(),    # autor
            'url': response.request.url,                                    # URL
            'tags': response.xpath('//tags').getall()                        # tags
        }
        
        # Salva estatísticas do crawling/scraping
        # self.crawler.stats.get_stats() - crawling stats
        # 
