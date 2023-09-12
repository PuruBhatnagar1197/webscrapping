import scrapy
from scrapy_splash import SplashRequest

class AdamcoiSpider(scrapy.Spider):
    name = "adamcoi"
    allowed_domains = ["www.adamchoi.co.uk"]
    # start_urls = ["http://www.adamchoi.co.uk/"]
    script=""" 
    function main(splash,args)
        splash.private_mode_disabled=false
        assert(splash:go(args.url))
        assert(splash:wait(5))
        all_matches=assert(splash:select_all("label.btn.btn-sm.btn-primary"))
        all_matches[2]:mouse_click()
        assert(splash:wait(5))
        splash:set_viewport_full()
        return {
            splash:png(),
            splash:html()
            }
    end    
    """

    def start_requests(self):
        yield SplashRequest(url="https://www.adamchoi.co.uk/overs/detailed",callback=self.parse,
                            endpoint='execute',args={'lua_source':self.script})
    def parse(self, response):
            rows=response.xpath('//tr')
            for row in rows:
                date=row.xpath('./td[1]/text()').get()
                home_team = row.xpath('./td[2]/text()').get()
                score = row.xpath('./td[3]/text()').get()
                away_team= row.xpath('./td[4]/text()').get()
                yield{
                    'date':date,
                    'home_team': home_team,
                    'score': score,
                    'away_team': away_team,
                }

