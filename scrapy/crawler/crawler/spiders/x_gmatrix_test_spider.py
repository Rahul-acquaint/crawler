import scrapy
import requests
import logging
from crawler import configs
from crawler.apis import APIEndpoints
from crawler.models.xeno_gtmetrix_test import GTMetrixModel

class GTMatrixTestSpider(scrapy.Spider):


    name="gt_matrix_check_test"
    url = APIEndpoints.x_gtmatrix_test
    GTMETRIX_API_KEY=configs.GTMETRIX_API_KEY

    def start_requests(self):
        url = self.url
        yield scrapy.Request(url=url)

    def store_xano_test_data(self, inputs:dict, maindb_id) -> None:
        data={
            "gtmetrix_grade" : inputs.get("gtmetrix_grade"),
            "performance_score" : inputs.get("performance_score"),
            "structure_score" : inputs.get("structure_score"),
            "largest_contentful_paint" : inputs.get("largest_contentful_paint"),
            "total_blocking_time" : inputs.get("total_blocking_time"),
            "cumulative_layout_shift" : inputs.get("cumulative_layout_shift"),
            "maindb_id" : maindb_id,
        }

        gtmatrix_model = GTMetrixModel()
        gtmatrix_model.add(data)
    
    def check_start(self, test_url, maindb_id): 
        auth = (self.GTMETRIX_API_KEY, '')
        response = requests.get(test_url, auth=auth)
        if  response.status_code == 200:
            response_data = response.json()
            attributes =  response_data.get("data", {}).get("attributes", {})
            self.store_xano_test_data(attributes, maindb_id)


    def parse(self, respose):
        test_sites= respose.json()
        for test_site in test_sites:
            self.check_start(test_site.get("link"), test_site.get("maindb_id"))
            