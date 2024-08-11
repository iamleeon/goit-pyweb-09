# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    tags = scrapy.Field()
    author = scrapy.Field()
    quote = scrapy.Field()


class AuthorsSpiderItem(scrapy.Item):
    fullname = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()
