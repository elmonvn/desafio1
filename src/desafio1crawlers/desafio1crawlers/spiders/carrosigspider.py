'''
Created on Nov 20, 2019

@author: elmonvn
'''

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from datetime import date, timedelta

class CarrosIgSpider(CrawlSpider):   
    hoje = str(date.today() - timedelta(days = 1))  
    name = 'carrosig'    
    start_urls = ['https://carros.ig.com.br/noticias']    
    rules = (        
        Rule(            
            LinkExtractor(allow=str("/" + hoje + "/"))        
        ),        
        Rule(            
            LinkExtractor(allow=str("/" + hoje + "/")), callback='parse_noticia')    
        )
        
    def parse_noticia(self, response):
        yield {
            'portal': self.name,
            'titulo': response.xpath('//h1[@id="noticia-titulo-h1"]/text()').extract_first(),        # título
            'corpo': (response.xpath('string(//div[@id="noticia"])').get()).strip(),                        # corpo
            'data': (response.xpath('//time[@itemprop="datePublished"]/text()').get().split(' '))[0],        # data
            'autor': response.xpath('//span[@id="authors-box"]/strong/text()').get(),    # autor
            'url': response.request.url,                                    # URL
            'tags': response.xpath('//tags').getall()                        # tags
        }
        
        # Salva estatísticas do crawling/scraping
        # self.crawler.stats.get_stats() - crawling stats
        # 
