import scrapy
import requests

from crawler import configs
from crawler.apis import APIEndpoints
from crawler.models.xano_gtmetrix_test import XanoGTMetrixTestModel
from crawler.models.xano_gtmetrix import XanoGTMetrixModel
from crawler.models.gt_metrix import GTMetrixTestModel

class GTMatrixTestSpider(scrapy.Spider):


    name="gt_matrix_check_test"
    url = APIEndpoints.x_gtmatrix_test
    GTMETRIX_API_KEY=configs.GTMETRIX_API_KEY

    def start_requests(self):
        url = self.url
        yield scrapy.Request(url=url)

    def store_xano_test_data(self, inputs:dict, maindb_id, test_site) -> None:
        data={
            "gtmetrix_grade" : inputs.get("gtmetrix_grade"),
            "performance_score" : inputs.get("performance_score"),
            "structure_score" : inputs.get("structure_score"),
            "largest_contentful_paint" : inputs.get("largest_contentful_paint"),
            "total_blocking_time" : inputs.get("total_blocking_time"),
            "cumulative_layout_shift" : inputs.get("cumulative_layout_shift"),
            "maindb_id" : maindb_id,
        }

        gtmatrix_model = XanoGTMetrixModel()
        gtmatrix_test_model =XanoGTMetrixTestModel()
        gtmatrix_model.add(data)      
        test_site["is_complete"]  =True
        gtmatrix_test_model.update(pk=test_site.get("id"), data=test_site)
    
    def check_start(self, test_url, maindb_id, test_site): 
        gt_metrixtest_model = GTMetrixTestModel()
        gt_metrixtest_model.url=test_url
        response_data = gt_metrixtest_model.get()
        if  response_data:
            attributes =  response_data.get("data", {}).get("attributes", {})
            self.store_xano_test_data(attributes, maindb_id, test_site)


    def parse(self, respose):
        test_sites = respose.json()
        for test_site in test_sites:
            self.check_start(test_site.get("link"), test_site.get("maindb_id"), test_site)
            