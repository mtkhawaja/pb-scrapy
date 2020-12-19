from scrapy.exporters import JsonLinesItemExporter
import datetime
class PasteItemJSONPipeline:
    def open_spider(self, spider):
        filename = self.generate_filename()
        self.backing_store = open(f'output/{filename}.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.backing_store)

    def close_spider(self, spider):
        self.backing_store.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def generate_filename(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")