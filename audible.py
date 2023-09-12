import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible" ## name of the spider
    allowed_domains = ["www.audible.com"] ## this should be the unique root domain of the website
    # start_urls = ["https://www.audible.com/search/"] ## this should be the url from which the data is to be extracted

    def start_requests(self):
        yield scrapy.Request(url="https://www.audible.com/search/",callback=self.parse,
                       headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})




    def parse(self, response):
        product_container=response.xpath('//div[@class="adbl-impression-container "]/div/span/ul/li')
        # product_container = response.xpath('//div[@class="adbl-impression-container "]/li')
        for product in product_container:
            book_title=product.xpath('.//h3[contains(@class,"bc-heading")]/a/text()').get()
            book_author = product.xpath('.//li[contains(@class,"authorLabel")]/span/a/text()').getall()
            book_length = product.xpath('.//li[contains(@class,"runtimeLabel")]/span/text()').get()

            yield{
                'title':book_title,
                'author':book_author,
                'length':book_length,
                'agent': response.request.headers['User-Agent']  ## to get which user agent we are using
            }
        ### handling pagination using scrappy
        pagination=response.xpath('//ul[contains(@class,"pagingElements")]')
        next_page_url=pagination.xpath('.//span[contains(@class,"nextButton")]/a/@href').get()

        if next_page_url:
            yield response.follow(url=next_page_url,callback=self.parse,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})


