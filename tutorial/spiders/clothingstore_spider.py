import scrapy


class ClothingstoreSpider(scrapy.Spider):
    name = "clothingstore"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        filename = f'clothingstore.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')