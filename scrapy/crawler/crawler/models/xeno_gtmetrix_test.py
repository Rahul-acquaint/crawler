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