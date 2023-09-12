import scrapy
import json


class QuotesSiteSpider(scrapy.Spider):
    name = "quotes_site"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        json_response=json.loads(response.body) ### by giving .body as a command it will give the complete response of the website with every tag and its value sone can simply just use the print(response.body) command to see the results
        quotes=json_response.get('quotes')
        for quote in quotes:

            yield{
                'author':quote.get('author').get('name'),
                'tags': quote.get('tags'),
                'quote': quote.get('text')

            }
        has_next=json_response.get('has_next')
        if has_next:
            next_page_number=json_response.get('page')+1
            yield scrapy.Request(
                url=f'https://quotes.toscrape.com/api/quotes?page={next_page_number}',
                callback=self.parse

            )
