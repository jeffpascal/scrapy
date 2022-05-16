import scrapy
# url response.css('div.box-anunt_row h2.titlu-anunt a::attr(href)').getall()
# titlu response.css('div.box-anunt_row h2.titlu-anunt span').get()
# all url-s to parse for info: response.css('div.box-anunt_row h2.titlu-anunt a::attr(href)').getall()
# inaintare la pagina urmatoare response.css('div.paginare a.inainte::attr(href)').getall()


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.imobiliare.ro/vanzare-apartamente/timis?id=275824403',
    ]

    def parse(self, response):
        for quote in response.css('div.box-anunt_row'):
            yield {
                'url': quote.css('h2.titlu-anunt a::attr(href)').get(),
                'titluAnunt': quote.css('h2.titlu-anunt span::text').get(),
            }

        next_page = response.css('div.paginare a.inainte::attr(href)').get()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)