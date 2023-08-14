import scrapy
import requests

from crawler import configs
from crawler.apis import APIEndpoints
from crawler.models.gt_metrix import GTMetrixModel
from crawler.models.xano_gtmetrix_test import XanoGTMetrixTestPostModel
from crawler.models.xano_maindb import XanoMainDBUpdateModel


class XanoMainDBSpider(scrapy.Spider):

    name="x_main_db"
    url = APIEndpoints.x_maindb_pagination
    
    def start_requests(self):
        url = self.url.format(1)
        yield scrapy.Request(url=url)

    def xeno_store(self, link, id):

        data ={
            "maindb_id":id,
            "link":link
        }
        xano_model = XanoGTMetrixTestPostModel()
        response_data = xano_model.post(data)

    def start_test(self, url, id):
        data = { "data": {
                "type": "test",
                "attributes": {"url":url,
                    "adblock":  1
                }}}
        gtmetrix_model = GTMetrixModel()
        response_data = gtmetrix_model.post(data)
        if response_data:
            test_link = response_data.get("links", {}).get("self", None)
            if test_link:
                self.xeno_store(test_link, id)



    def parse(self, respose):
        response_data = respose.json()
            
        items = response_data.get("items", [])
        site_webs = [{"url":item.get("site_web"), "id":item.get("id")} for item in items]

        for site in site_webs:
            self.start_test(**site)
            xano_update_model = XanoMainDBUpdateModel()
            response_data

        for item in  items:
            pk=item.get("id")
            xano_update_model.update_timespamp(item, pk)



