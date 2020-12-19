# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

def serialize_content(value):
    return value.decode()

class PasteItem(Item):
    scrape_url = Field()
    full_url = Field()
    date = Field()
    key = Field() 
    size = Field()
    expire = Field()
    title = Field() 
    syntax = Field()
    user = Field()
    hits = Field()
    content = Field(serializer=serialize_content)
