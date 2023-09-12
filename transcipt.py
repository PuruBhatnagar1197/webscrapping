import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TransciptSpider(CrawlSpider):
    name = "transcipt"
    allowed_domains = ["subslikescript.com"]
    # start_urls = ["https://subslikescript.com/movies_letter-J"]
    user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url='https://subslikescript.com/movies_letter-J',
                             headers={'user-agent':self.user_agent})

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback="parse_item", follow=True,process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]")),process_request='set_user_agent')  ### this is for pagination and also to change the user agent
             )

    def set_user_agent(self,request,spider):
        request.headers['user-Agent']=self.user_agent
        return request

    def parse_item(self, response):
        # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")
        ## below step when trying sqlite
        transcript_list=article.xpath("./div[@class='full-script']/text()").getall()
        transcript_string=" ".join(transcript_list)

        # Extract the data we want and then yield it
        yield {
            'title': article.xpath("./h1/text()").get(),
            'plot': article.xpath("./p/text()").get(),
            'transcript':transcript_string,
            'url': response.url,
            # 'user_agent':response.request.headers['user-Agent']
        }
