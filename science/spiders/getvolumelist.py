# -*- coding: utf-8 -*-
import scrapy
from ..items import ScienceItem


class GetvolumelistSpider(scrapy.Spider):
    name = 'getvolumelist'
    start_urls = ['https://link.springer.com/journal/11340/volumes-and-issues']

    def parse(self, response):
        items = ScienceItem()
        raw_volume_list = response.css('.u-interface-link::attr(href)').extract()
        for url_list in raw_volume_list:
            volume_url = url_list
            items['volume_list'] = 'https://link.springer.com/' + volume_url
            yield items
