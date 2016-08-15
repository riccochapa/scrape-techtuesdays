import scrapy

from techtuesdays.items import TechTuesdaysItem

class TechTuesdaysSpider(scrapy.Spider):
    name = "techtuesdays"
    allowed_domains = ["techtuesdays.co"]
    start_urls = [
        "http://www.techtuesdays.co",
    ]

    def parse(self, response):
        for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            item = TechTuesdaysItem()
            link = sel.xpath('a/@href').extract()
            yield item
