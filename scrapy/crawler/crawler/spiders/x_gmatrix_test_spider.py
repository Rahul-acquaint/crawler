import scrapy
import requests

from crawler import configs
from crawler.apis import APIEndpoints
from crawler.models.xano_gtmetrix_test import XanoGTMetrixTestModel
from crawler.models.xano_gtmetrix import XanoGTMetrixModel
from crawler.models.gt_metrix import GTMetrixTestModel

class GTMatrixTestSpider(scrapy.Spider):


    name="gt_matrix_check_test"
    url = APIEndpoints.x_gtmatrix
    GTMETRIX_API_KEY=configs.GTMETRIX_API_KEY

    def start_requests(self):
        url = self.url
        yield scrapy.Request(url=url)

    def store_xano_test_data(self, inputs, data, links):
        data["gtmetrix_grade"] = inputs.get("gtmetrix_grade")
        data["performance_score"] = inputs.get("performance_score")
        data["structure_score"] = inputs.get("structure_score")
        data["largest_contentful_paint"] = inputs.get("largest_contentful_paint")
        data["total_blocking_time"] = inputs.get("total_blocking_time")
        data["cumulative_layout_shift"] = inputs.get("cumulative_layout_shift")
        data["gtmetrix_pdf"] = links.get("report_pdf")
        data["is_complete"] = True

        gtmatrix_test_model = XanoGTMetrixTestModel()
        gtmatrix_test_model.update(pk=data.get("id"), data=data)
    
    def check_start(self, test_url, test_site): 
        gt_metrixtest_model = GTMetrixTestModel()
        gt_metrixtest_model.url=test_url
        response_data = gt_metrixtest_model.get()
        if  response_data:
            attributes =  response_data.get("data", {}).get("attributes", {})
            links =  response_data.get("data", {}).get("links", {})
            self.store_xano_test_data(attributes, test_site, links)


    def parse(self, respose):
        test_sites = respose.json()
        test_sites = test_sites.get("items")
        for test_site in test_sites:
            self.check_start(test_site.get("link"), test_site)
            