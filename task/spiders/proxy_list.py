import scrapy
import re

from task.items import TaskItem


class ProxyListSpider(scrapy.Spider):
    name = "proxy_list"
    allowed_domains = ["free-proxy.cz"]
    start_urls = ["http://free-proxy.cz/en/"]
    custom_settings = {
        "FEEDS": {
            "proxy_data.json": {
                "format": "json",
                "overwrite": True,
            }
        }
    }

    def parse(self, response):
        items_rows = response.xpath("//table[@id='proxy_list']/tbody/tr")
        for row in items_rows:
            script_tag_string = row.xpath(".//td[1]/script").get()
            ip_address = re.search(
                r'Base64.decode\("(.*?)\"\)\)</script>', script_tag_string
            )
            if ip_address is not None:
                task_item = TaskItem()
                task_item["port"] = row.xpath(".//td[2]/span//text()").get()
                task_item["ip_address"] = ip_address.group(1)

                yield task_item
