'''
Created on Nov 20, 2019

@author: elmonvn
'''

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class QuatroRodasSpider(CrawlSpider):     
    name = 'quatrorodas'    
    start_urls = ['https://quatrorodas.abril.com.br/noticias/']    
    rules = (        
        Rule(            
            LinkExtractor(allow='/noticias/')        
        ),        
        Rule(            
            LinkExtractor(allow='/noticias/',), callback='parse_noticia')    
        )
        
    def parse_noticia(self, response):
        yield {
            'portal': self.name,
            'titulo': response.xpath('//h1[@class="article-title"]/text()').extract_first(),        # título
            'corpo': (response.xpath('string(//section[@class="article-content"])').get()).strip(),                        # corpo
            'data': (response.xpath('//div[@class="article-date"]//span/text()').get().split('-'))[0],        # data
            'autor': response.xpath('//div[@class="article-author-name"]//strong/text()').get(),    # autor
            'url': response.request.url,                                    # URL
            'tags': response.xpath('//section[@class="article-tags"]/a[@rel="tag"]').getall()                        # tags
        }
        
        # Salva estatísticas do crawling/scraping
        # self.crawler.stats.get_stats() - crawling stats
        # 
