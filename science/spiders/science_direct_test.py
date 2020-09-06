import scrapy
import json
import re
from ..items import Get_List_Item


class QuoteSpider(scrapy.Spider):
    name = 'get_article_list'
    try:
        with open("volume_list.json", "r") as f:
            urls_data = json.load(f)
        start_urls = []
        for volume_url in urls_data:
            start_urls.append(volume_url['volume_list'])
    except:
        print('no volume list yet')

    def parse(self, response):
        items = Get_List_Item()
        all_article_list = response.css('.c-card__title a')
        for paper in all_article_list:
            article_name = paper.css('::text').extract()[0]
            article_link = paper.css('::attr(href)').extract()[0]
            items['article_name'] = article_name
            items['article_link'] = article_link
            yield items
        next_page = response.css('.next::attr(href)').extract()
        print(next_page)
        if next_page:
            print("im am in next page")
            next_page_url = 'https://link.springer.com' + next_page[0]
            yield scrapy.Request(url=next_page_url, callback=self.parse)
        # yield {
        #         'key': keyword_test
        # }
