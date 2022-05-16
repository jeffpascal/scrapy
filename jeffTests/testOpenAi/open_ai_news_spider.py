import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://openai.com/blog/',
    ]

    def parse(self, response):
        print(response)
        print(response.css)
        for quote in response.css('div.post-card-full'):
            yield {
                'author': quote.xpath('span/small/text()').get(),
                # Select a div with the post-card-full classname then the h5 element inside then the attr of a. If it was an id, i would have used the # separator
                'text': quote.css('div.post-card-full').getAll(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            