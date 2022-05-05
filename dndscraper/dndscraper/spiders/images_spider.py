import scrapy
from scrapy.selector import Selector

class ImagesSpider(scrapy.Spider):
    name = "images"
    
    def start_requests(self):
        base_url = 'https://www.google.nl/search?q='
        search_url = '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjen5y2h8j3AhVnqFYBHcbeBIoQ_AUoAXoECAMQAw&cshid=1651743355084032&biw=1440&bih=686&dpr=2'
        params = 'sexy'
        full_url = base_url + params + search_url
        urls = [
                full_url
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        response.css('.rg_i Q4LuWd img::attr(src)').extract_first()
        page = response.url.split("/")[-2]
        filename = f'images-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')