import scrapy, json
from scrapy import Request
from .. import settings, items

class PBSpider(scrapy.Spider):
    name = "PBSpider"

    def start_requests(self):
        urls = [settings.RECENT_PASTES_ENDPOINT]
        for url in urls:
            yield Request(url=url, callback=self.parse_paste_list)

    def parse_paste_list(self, response):
        recent_paste_list = json.loads(response.body)
        for paste in recent_paste_list:
            yield Request(url=paste['scrape_url'], callback=self.parse_paste_contents, meta={'paste_item': paste})

    def parse_paste_contents(self, response):
        paste_item = items.PasteItem(response.meta.get('paste_item'))
        paste_item['content'] = response.body
        yield paste_item