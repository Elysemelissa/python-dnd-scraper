import scrapy
from dndscraper.items import DndscraperItem

# from scrapy.selector import Selector

class ImagesSpider(scrapy.Spider):
    name = "images"
    
    def start_requests(self):
        base_url = 'https://www.google.nl/search?q='
        search_url = '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjen5y2h8j3AhVnqFYBHcbeBIoQ_AUoAXoECAMQAw&cshid=1651743355084032&biw=1440&bih=686&dpr=2'
        params = 'druid'
        full_url = base_url + params + search_url
        urls = [
                full_url
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        images = response.xpath("//*[@class='.Q4LuWd']")
        for image in images:
            image_link = image.xpath(".//img/@src").get() 
            yield response.follow(image_link, callback=self.scrape_image) 
        
    def scrape_image(self, response):
        item = DndscraperItem()
        item['image_binary'] = response.body
        return item
        # 
        #  response.css('.rg_i Q4LuWd img::attr(src)').extract_first()
        # page = response.url.split("/")[-2]
        # filename = f'images-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}' 
        