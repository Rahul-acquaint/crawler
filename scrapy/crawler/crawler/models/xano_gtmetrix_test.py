from crawler.apis import APIEndpoints

from crawler import configs
from crawler.models.abstract_model import AbstractModel
from crawler.debugger import Debugger


class XanoGTMetrixTestModel(AbstractModel):

    url = APIEndpoints.x_gtmatrix_test

    def update(self, pk, data):
        self.pk = pk
        response = super().post(data)
        data = response.json
        if response.status_code == 200:...
        else:
            Debugger.error("error ", data, response.url)
        return data
        
    
    def get_post(self):
        url = f"{self.url}/{self.pk}"
        return url


class XanoGTMetrixTestPostModel(AbstractModel):

    url = APIEndpoints.x_gtmatrix_test

    def post(self, data):
        response = super().post(data)
        if response.status_code == 200:...
        else:
            Debugger.error("error ", data, response.url)
        return data
        