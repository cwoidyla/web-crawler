# -*- coding: utf-8 -*-
import scrapy


class SentimentSpider(scrapy.Spider):
    name = 'sentiment'
    allowed_domains = ['https://money.cnn.com/data/fear-and-greed']
    start_urls = ['https://money.cnn.com/data/fear-and-greed/']

    def parse(self, response):
        sentiment = '//*[@id="fearGreedContainer"]/div/div[4]'
        subsentiment = '//div[%s]/div[2]/div[1]/p[2]/span/text()'
        data = response.xpath(sentiment)
        for i in range(1,8): 
            yield {
                'sentiment' : data.xpath(subsentiment % str(i)).get()
            }
