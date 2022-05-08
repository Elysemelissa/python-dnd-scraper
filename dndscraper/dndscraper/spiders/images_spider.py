import scrapy
from dndscraper.items import DndscraperItem

# from scrapy.selector import Selector

class ImagesSpider(scrapy.Spider):
    name = "images"
    
    def start_requests(self):
        base_url = 'https://www.dndbeyond.com/monsters'
        # search_url = '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjen5y2h8j3AhVnqFYBHcbeBIoQ_AUoAXoECAMQAw&cshid=1651743355084032&biw=1440&bih=686&dpr=2'
        # params = 'druid'
        # user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        full_url = base_url
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        urls = [
                full_url
            ]
        for url in urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        images = response.xpath('//div[@class="image"]/@style').re(r'url\((.*)\);')
        
        yield {'images': images}
        
    def scrape_image(self, response):
        item = DndscraperItem()
        item['image_binary'] = response.body
        return item
        