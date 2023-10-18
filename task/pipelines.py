# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import base64


class TaskPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter["ip_address"] = base64.b64decode(adapter.get("ip_address")).decode(
            "utf-8"
        )
        adapter["port"] = int(adapter.get("port"))

        return item
