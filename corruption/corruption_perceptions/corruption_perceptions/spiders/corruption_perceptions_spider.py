import scrapy


class CorruptionPerceptionsSpiderSpider(scrapy.Spider):
    name = "corruption_perceptions_spider"
    allowed_domains = ["www.transparency.org"]
    start_urls = ["https://www.transparency.org/en/cpi/2022"]

    def start_requests(self):
        return super().start_requests()

    def parse(self, response):
        for link in response.css("[aria-label='Select a country'] > option ::attr(value)"):
            yield response.follow(link.get(), callback=self.grab_cpi)

    def grab_cpi(self, response):
        cpi_dict = {}
        cpi_dict[response.css("title::text").extract()[0]] = response.css("[aria-labelledby='country-data']>div>section:nth-child(1)>div>div:nth-child(2)>p:nth-child(2)::text").extract()[0]
        return cpi_dict
