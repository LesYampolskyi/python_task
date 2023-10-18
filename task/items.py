# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaskItem(scrapy.Item):
    ip_address = scrapy.Field()
    port = scrapy.Field()
