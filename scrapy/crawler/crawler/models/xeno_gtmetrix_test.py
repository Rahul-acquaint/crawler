from crawler.apis import APIEndpoints

from crawler import configs
from crawler.models.abstract_model import AbstractModel
from crawler.debugger import Debugger

class GTMetrixModel(AbstractModel):

    url = APIEndpoints.x_gtmatrix

    def add(self, data):

        response = self.post(data)
        data = response.json
        if response.status_code == 200:
            Debugger.info("xeno test save successfully")
        else:
            Debugger.error("error ", data)



class GTMetrixTestModel(AbstractModel):

    url = APIEndpoints.x_gtmatrix_test

    def update(self, pk, data):
        self.pk = pk
        response = self.post(data)
        data = response.json
        if response.status_code == 200:
            Debugger.info("xeno test updated successfully")
        else:
            Debugger.error("error ", data, response.url)

        
    
    def get_post(self):
        url = f"{self.url}/{self.pk}"
        return url


