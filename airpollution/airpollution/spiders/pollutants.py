import scrapy


class PollutantsSpider(scrapy.Spider):
    name = "pollutants"
    start_urls = ["https://naei.beis.gov.uk/overview/ap-overview"]

    def start_requests(self):
        return super().start_requests()

    def parse(self, response):
        for link in response.css('div > ul > li > a ::attr(href)'):
            if link.extract().find('pollutants') != -1:
                yield response.follow(link.get(), callback=self.parse_pollutant)
    
    def parse_pollutant(self,response):
        pollutant_sources = response.css('.sector-selection > option ::text').extract()
        pollutant_name = response.css('.mainblock::text').extract()
        pollutant_category = response.css('.bold::text').extract()
        pollutant_info = {"Pollutant":pollutant_name,"Category":pollutant_category,"Sources":pollutant_sources}
        yield pollutant_info