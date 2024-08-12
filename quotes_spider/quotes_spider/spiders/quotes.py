import scrapy

from ..items import QuotesSpiderItem, AuthorsSpiderItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response, **kwargs):
        for quote in response.xpath("/html//div[@class='quote']"):
            tags = quote.xpath("div[@class='tags']/a/text()").extract()
            author = quote.xpath("span/small[@class='author']/text()").get()
            quote_text = quote.xpath("span[@class='text']/text()").get()
            yield QuotesSpiderItem(
                tags=tags,
                author=author,
                quote=quote_text
            )

            yield response.follow(url=self.start_urls[0] + quote.xpath("span/a/@href").get(), callback=self.parse_author)

            next_link = response.xpath("//li[@class='next']/a/@href").get()
            if next_link:
                yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_author(self, response):
        fullname = response.xpath("/html//h3[@class='author-title']/text()").get()
        born_date = response.xpath("/html//span[@class='author-born-date']/text()").get()
        born_location = response.xpath("/html//span[@class='author-born-location']/text()").get()
        description = response.xpath("/html//div[@class='author-description']/text()").get().strip()

        yield AuthorsSpiderItem(
            fullname=fullname,
            born_date=born_date,
            born_location=born_location,
            description=description
        )
