import codecs
import hashlib
# from configuration import urls, domains
from lxml import html
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from telangana.helpers.xpath_text import dump_text
from telangana.helpers.configuration import urls, domains
import sys
from time import sleep
import os
import requests
import traceback

reload(sys)
sys.setdefaultencoding('utf-8')
Type = sys.getfilesystemencoding()
path = "../data/"
filename = ""
# f = codecs.open("../data/mygov.txt", "a", "utf-8")


class MySpider(CrawlSpider):
    name = 'crawler'
    start_urls = urls
    allowed_domains = domains

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        url = response.url

        # if ".in/agriculture" in url or ".in/health" in url or ".in/education" in url or ".in/social-welfare" in url or ".in/rural-energy" in url or ".in/e-governance" in url:
        url = response.url
        # f.write(url + "\n")
        # sleep(2020000000
        item = dict()
        item['url'] = response.url
        item['title'] = response.meta['link_text']
        # extracting basic body
        item['body'] = '\n'.join(response.xpath('//text()').extract())
        # or better just save whole source
        item['source'] = response.body
        url = response.url
        dump = dump_text(response.body)
        if "www" in response.url:
            filename = response.url.split(".")[1]
        else:
            filename = response.url.split(".")[0].split("//")[1]
        if "/as/" in url:
            print "url ----->" + url
            f = codecs.open(path + filename, "a", "utf-8")
            f.write(dump + "\n")

